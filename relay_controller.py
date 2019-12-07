import boto3
from time import sleep
import RPi.GPIO as GPIO
from random import randint, choice

GPIO.setmode(GPIO.BCM)

# OUTLET -> GPIO
OUT1 = 2
OUT2 = 3
OUT3 = 4
OUT4 = 17
OUT5 = 27
OUT6 = 22
OUT7 = 10
OUT8 = 9

# PINS
SANTA_HOUSE = OUT6
ELVES_BUNK = OUT1
POST_OFFICE = OUT2
REINDEER_STABLES = OUT7
TREE = OUT8
TRAIN = OUT4
C9 = OUT5

# Modes
ALL = 99
DISCO = 1337
WIZARDS = 7331
DUCK_DUCK_GOOSE = 7332
OFF = 7300


# Input to Pins Dict
input_pin_dict = {
    'SANTA_HOUSE':SANTA_HOUSE,
    'ELVES_BUNK': ELVES_BUNK,
    'POST_OFFICE': POST_OFFICE,
    'REINDEER_STABLES': REINDEER_STABLES,
    'TREE': TREE,
    'TRAIN': TRAIN,
    'ALL': ALL,
    'DISCO': DISCO,
    'WIZARDS': WIZARDS,
    'C9': C9,
    'DUCK_DUCK_GOOSE': DUCK_DUCK_GOOSE,
    'OFF': OFF
    }

pin_list = [
    SANTA_HOUSE,
    ELVES_BUNK,
    POST_OFFICE,
    REINDEER_STABLES,
    TREE,
    C9,
    TRAIN
]

disco_pin_list = pin_list[:-1]


class InvalidInputException(Exception):
    pass


def init_gpio():
    for i in pin_list:
        GPIO.setup(i, GPIO.OUT)


def parse_input_to_pin(input):
    input = input.upper()

    if input not in input_pin_dict:
        raise InvalidInputException()

    print(input)
    return input_pin_dict[input]


def blink(delay=0.2):
    turn_on_all_relays()
    sleep(delay)
    turn_off_all_relays()

def duck_duck_goose():
    set_relay(C9)
    pins = [ELVES_BUNK, REINDEER_STABLES, SANTA_HOUSE, TREE, POST_OFFICE]
    for _ in range(4):
        for p in pins:
            sleep(0.1)
            set_relay(p)
            sleep(0.1)
            set_relay(p)

def five_key_piano():
    for i in range(34):
        sleep(0.075)
        turn_off_all_relays()
        sleep(0.075)
        turn_on_all_relays()

def guitar_riff(delay=0.3):
    for _ in range(18):
        set_relay(C9)
        sleep(delay)
        set_relay(C9)
        sleep(delay)

def down_piano(delay=0.15):
    pin_list = [
        POST_OFFICE,
        TREE,
        SANTA_HOUSE,
        REINDEER_STABLES,
        ELVES_BUNK,
        REINDEER_STABLES,
        SANTA_HOUSE,
        TREE
    ]

    piano_n(pin_list, delay)

def prance_piano(delay=0.2):
    # TODO: Figure out what to do for this:
    # piano() leaves lights on
    # down_piano() doesn't
    piano(delay)
    down_piano(delay)
    piano(delay)
    down_piano(delay)

def piano_n(pin_list, delay=0.1):
    set_relay(C9)
    for p in pin_list:
        set_relay(p)
        sleep(delay)
        set_relay(p)
        sleep(delay)

def piano4():
    p4 = [ELVES_BUNK, REINDEER_STABLES, SANTA_HOUSE, TREE]
    piano_n(p4)

def piano9():
    p9 = [ELVES_BUNK, REINDEER_STABLES, SANTA_HOUSE, TREE, POST_OFFICE, TREE, SANTA_HOUSE, REINDEER_STABLES]
    piano_n(p9)

def piano_4_4_9():
    turn_off_all_relays()
    piano4()
    piano4()
    piano9()

def b2b2b1():
    blink(delay=0.1)
    blink(delay=0.1)
    sleep(0.2)
    blink(delay=0.1)
    blink(delay=0.1)
    sleep(0.2)
    blink()

def set_relay(pin):
    if pin == ALL:
        turn_on_all_relays()
        return

    if GPIO.input(pin) == None:
        print('pin {} is None'.format(pin))

    if GPIO.input(pin) == 1:
        GPIO.output(pin, GPIO.LOW)
    else:
        GPIO.output(pin, GPIO.HIGH)

def wizards_main():
    for i in range(6): triple_beat()
    piano()
    for i in range(6): triple_beat()
    piano()
    # alt_back_forth(delay=0.3)
    for i in range(6): alt_back_forth()
    blink()
    piano()
    for i in range(6): alt_back_forth()
    blink()
    piano()
    blink()
    piano()
    b2b2b1() # 0:29
    blink()
    blink()

    print('0:32')
    for i in range(6): alt_back_forth() # 0:32
    blink()
    piano()
    print('0:38')
    for i in range(6): alt_back_forth() # 0:38
    blink()
    piano()
    blink()
    piano()
    blink()
    b2b2b1()
    print('0:48')
    down_piano() # 0:48
    print('0:51')
    guitar_riff() # 0:51 # should continue through piano_4_4_9
    print('0:58')
    piano_4_4_9() # 0:58
    print('1:04')
    piano_4_4_9()  # 1:04
    print('1:10')
    blink() # 1:10
    piano()
    blink()
    piano()
    blink()
    b2b2b1()
    print('1:17')
    for i in range(6): alt_back_forth() # 1:17
    blink()
    piano()
    print('1:24')
    for i in range(6): alt_back_forth() # 1:24
    blink()
    piano()
    print('1:30')
    blink() # 1:30
    piano()
    print('1:32')
    blink() # 1:32
    piano()
    down_piano()
    prance_piano()
    print('1:39')
    guitar_riff() # 1:39
    # bg vocals
    print('2:07')
    blink() # 2:07
    piano()
    blink()
    piano()
    print('2:10')
    blink() # 2:10
    ###
    print('2:10')
    b2b2b1() # 2:10  -- actually written as b2b2b1b1b1
    blink()
    blink()
    ###
    print('2:12')
    for i in range(6): alt_back_forth()  # 2:12
    print('2:18')
    blink() # 2:18
    piano()
    print('2:19')
    for i in range(6): alt_back_forth()  # 2:19
    blink()
    print('2:24 -> 2:30')
    #diag piano # 2:24 -> 2:30
    print('2:26')
    blink()  # 2:26
    print('2:27')
    blink()  # 2:27
    print('2:28')
    blink()  # 2:28
    print('2:29')
    blink()  # 2:29
    print('2:30')
    #b4 # 2:30
    print('2:30')
    for i in range(6): alt_back_forth()  # 2:30
    print('2:45 -> 2:52')
    five_key_piano()  # 2:45 -> 2:52
    print('2:59 -> 3:02')
    duck_duck_goose() # 2:59 -> 3:02
    blink() #end 3:02

    sleep(3)
    turn_on_all_relays()


def triple_beat(delay=0.1):
    turn_off_all_relays()

    for _ in range(3):
        sleep(delay)
        turn_on_all_relays()
        sleep(delay)
        turn_off_all_relays()

def piano(delay=0.2):
    turn_off_all_relays()

    sleep(delay)
    set_relay(ELVES_BUNK)
    sleep(delay)
    set_relay(REINDEER_STABLES)
    sleep(delay)
    set_relay(SANTA_HOUSE)
    sleep(delay)
    set_relay(TREE)
    sleep(delay)
    set_relay(POST_OFFICE)
    sleep(delay)

    turn_off_all_relays()
    sleep(0.1)
    turn_on_all_relays()
    sleep(0.5)

def alt_back_forth(delay=0.15):
    turn_off_all_relays()
    set_relay(C9)
    wizard_pins = [ELVES_BUNK, REINDEER_STABLES, SANTA_HOUSE, TREE, POST_OFFICE]

    for pin in wizard_pins:
        set_relay(pin)
        sleep(delay)
        set_relay(pin)

    for pin in reversed(wizard_pins):
        set_relay(pin)
        sleep(delay)
        set_relay(pin)

def turn_off_all_relays():
    # use disco pin list to avoid rapid on/off of train
    for pin in disco_pin_list:
        GPIO.output(pin, GPIO.HIGH)


def turn_on_all_relays():
    # use disco pin list to avoid rapid on/off of train
    for pin in disco_pin_list:
        GPIO.output(pin, GPIO.LOW)


def disco_mode():
    count = 120
    while count > 0:
        r = randint(0, len(disco_pin_list)-1)
        pin = disco_pin_list[r]
        set_relay(pin)
        count -= 1
        sleep(0.1)

    turn_on_all_relays()
    sleep(0.5)
    turn_off_all_relays()
    sleep(0.5)
    turn_on_all_relays()
    sleep(0.5)
    turn_off_all_relays()
    sleep(0.5)
    turn_on_all_relays()


def duck_duck_goose_st(delay=0.25):
    pins = disco_pin_list
    for _ in range(4):
        for p in pins:
            sleep(delay)
            set_relay(p)
            sleep(delay)
            set_relay(p)


def get_sqs():
    sqs = boto3.resource('sqs',
                         region_name='',
                         aws_secret_access_key='',
                         aws_access_key_id='',
                         use_ssl=True)
    queue = sqs.Queue('')
    return queue


def pick_random_action():
    actions = [DISCO, WIZARDS, DUCK_DUCK_GOOSE]
    random_action = choice(actions)

    print("Random action: " + random_action)

    if random_action == WIZARDS:
        wizards_main()
    elif random_action == DISCO:
        disco_mode()
    elif random_action == DUCK_DUCK_GOOSE:
        duck_duck_goose_st()


def main():
    init_gpio()
    queue = get_sqs()

    max_count_before_random_action = 10
    pick_interaction_counter = 0

    while True:
        sleep(3)
        messages = queue.receive_messages()

        if pick_interaction_counter >= max_count_before_random_action:
            pick_random_action()
            pick_interaction_counter = 0

        if len(messages) == 0:
            pick_interaction_counter += 1
            continue

        msg = messages[0]

        try:
            print(msg.body)
            pin = parse_input_to_pin(msg.body)
        except InvalidInputException as ex:
            print(ex)
            msg.delete()
            continue

        msg.delete()

        if pin == WIZARDS:
            wizards_main()
        elif pin == DISCO:
            disco_mode()
        elif pin == DUCK_DUCK_GOOSE:
            duck_duck_goose_st()
        elif pin == OFF:
            turn_off_all_relays()
        else:
            set_relay(pin)



if __name__ == '__main__':
    main()
