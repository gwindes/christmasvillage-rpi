"""
Copyright 2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the 'License'). You may not use this file except in compliance with the License. A copy of the License is located at

    http://aws.amazon.com/apache2.0/

or in the 'license' file accompanying this file. This file is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
"""

import sys
import irc.bot
import requests
import boto3


class InvalidVote(Exception):
    pass

class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, username, client_id, token, channel):
        self.client_id = client_id
        self.token = token
        self.channel = '#' + channel

        self.vote_types = ['all', 'disco', 'tree', 'santa', 'postoffice', 'elves', 'reindeer', 'train']
        self.votes = dict()
        self.users_voted = set()

        self.reset_votes()

        # Get the channel id, we will need this for v5 API calls
        url = 'https://api.twitch.tv/kraken/users?login=' + channel
        headers = {'Client-ID': client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
        r = requests.get(url, headers=headers).json()
        self.channel_id = r['users'][0]['_id']

        # Create IRC bot connection
        server = 'irc.chat.twitch.tv'
        port = 6667
        print()
        'Connecting to ' + server + ' on port ' + str(port) + '...'
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, 'oauth:' + token)], username, username)


    def reset_votes(self):
        for type in self.vote_types:
            self.votes[type] = 0

        self.users_voted = set()

    def on_welcome(self, c, e):
        print()
        'Joining ' + self.channel

        # You must request specific capabilities before you can use them
        c.cap('REQ', ':twitch.tv/membership')
        c.cap('REQ', ':twitch.tv/tags')
        c.cap('REQ', ':twitch.tv/commands')
        c.join(self.channel)

    def on_pubmsg(self, c, e):

        # If a chat message starts with an exclamation point, try to run it as a command
        if e.arguments[0][:1] == '!':
            cmd = e.arguments[0].split(' ')[0][1:]
            print()
            'Received command: ' + cmd
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
            raise InvalidVote('You have already voted. You can vote again in {} seconds'.format('TBD'))

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

    bot = TwitchBot(username, client_id, token, channel)
    bot.start()


if __name__ == '__main__':
    main()