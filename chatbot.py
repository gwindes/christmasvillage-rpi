import sys
import irc.bot
import requests
import boto3
from irc.schedule import DefaultScheduler
import uuid
import time
import os

VOTE_DURATION = 60


class InvalidVote(Exception):
    pass


class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, username, client_id, token, channel):
        self.client_id = client_id
        self.token = token
        self.channel = '#' + channel

        self.vote_translation = {
            'all': 'ALL',
            'disco': 'DISCO',
            'tree': 'TREE',
            'santa': 'SANTA_HOUSE',
            'postoffice': 'POST_OFFICE',
            'elves': 'ELVES_HOUSE',
            'reindeer': 'REINDEER_STABLES',
            'train': 'TRAIN'
        }
        self.vote_types = self.vote_translation.keys()
        self.votes = dict()
        self.users_voted = set()

        self.reset_votes()
        self.last_vote_cast_time = time.time()

        # Get the channel id, we will need this for v5 API calls
        url = 'https://api.twitch.tv/kraken/users?login=' + channel
        headers = {'Client-ID': client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
        r = requests.get(url, headers=headers).json()
        self.channel_id = r['users'][0]['_id']

        # Create IRC bot connection
        server = 'irc.chat.twitch.tv'
        port = 6667
        'Connecting to ' + server + ' on port ' + str(port) + '...'
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, 'oauth:' + token)], username, username)

    def tally_votes(self):
        print('Counting votes')
        max_count = 0
        voted_type = None

        for vote_type in self.vote_types:
            if self.votes[vote_type] > max_count:
                max_count = self.votes[vote_type]
                voted_type = vote_type

        if voted_type is not None:
            self.msg_vote(voted_type, max_count)
            self.send_vote_to_sqs(voted_type)
            self.reset_votes()

    def msg_vote(self, vote, count):
        c = self.connection
        c.privmsg(self.channel, 'Casting vote: {} with {} votes'.format(vote, count))

    def send_vote_to_sqs(self, vote):
        print('Sending {} to village'.format(vote))
        sqs = boto3.resource('sqs',
                             region_name='us-east-1',
                             aws_secret_access_key=os.getenv('AWS_SECRET', ''),
                             aws_access_key_id=os.getenv('AWS_KEY', ''),
                             use_ssl=True)
        queue = sqs.Queue(os.getenv('SQS_QUEUE', ''))
        v = self.vote_translation[vote]
        queue.send_message(MessageBody=v, MessageGroupId='1', MessageDeduplicationId=str(uuid.uuid4()))
        return queue

    def reset_votes(self):
        for vote_type in self.vote_types:
            self.votes[vote_type] = 0

        self.users_voted = set()
        self.last_vote_cast_time = time.time()

    def on_welcome(self, c, e):
        print('Joining ' + self.channel)

        # You must request specific capabilities before you can use them
        c.cap('REQ', ':twitch.tv/membership')
        c.cap('REQ', ':twitch.tv/tags')
        c.cap('REQ', ':twitch.tv/commands')
        c.join(self.channel)

    def on_pubmsg(self, c, e):
        # If a chat message starts with an exclamation point, try to run it as a command
        if e.arguments[0][:1] == '!':
            cmd = e.arguments[0].split(' ')[0][1:]
            # print('Received command: ' + cmd)
            self.do_command(e, cmd)
        return

    def parse_vote_event(self, event):
        param = event.arguments[0].lower()
        vote = param.split(' ')[1]

        if vote not in self.vote_types:
            valid_types = ' | '.join(self.vote_types)
            raise InvalidVote('Invalid vote type: {} Try from the following: {}'.format(vote, valid_types))

        return vote

    def parse_user_id(self, event):
        return event.tags[11]['value']

    def handle_vote(self, vote, user):
        if user in self.users_voted:
            seconds_until_vote_allowed = VOTE_DURATION - (time.time() - self.last_vote_cast_time)
            raise InvalidVote('You have already voted. You can vote again in {:.0f} seconds'.format(seconds_until_vote_allowed))

        if vote in self.votes:
            self.votes[vote] += 1
            self.users_voted.add(user)
            print(vote, user)

    def do_command(self, event, cmd):
        c = self.connection

        if cmd == 'vote':
            try:
                vote = self.parse_vote_event(event)
                user_id = self.parse_user_id(event)
                self.handle_vote(vote, user_id)
                c.privmsg(self.channel, 'Added your vote {}'.format(vote))
            except InvalidVote as ex:
                c.privmsg(self.channel, str(ex))
        else:
            c.privmsg(self.channel, 'Did not understand command: ' + cmd)
            c.privmsg(self.channel, 'Try: !vote elves')


def main():
    if len(sys.argv) != 5:
        print('Usage: twitchbot <username> <client id> <token> <channel>')
        sys.exit(1)

    username = sys.argv[1]
    client_id = sys.argv[2]
    token = sys.argv[3]
    channel = sys.argv[4]

    scheduler = DefaultScheduler()

    bot = TwitchBot(username, client_id, token, channel)
    scheduler.execute_every(VOTE_DURATION, bot.tally_votes)
    bot.reactor.scheduler = scheduler
    bot.start()


if __name__ == '__main__':
    main()
