# for desktop only uncomment for local dev
# import sys
# import fake_rpi

# sys.modules['RPi'] = fake_rpi.RPi
# sys.modules['RPi.GPIO'] = fake_rpi.RPi.GPIO

# actual imports
import os
import boto3
import RPi.GPIO as GPIO
import phpserialize as ps
import json

# auto load env variables from .env file
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from botocore.exceptions import ClientError
from time import sleep
from random import randint, choice


GPIO.setmode(GPIO.BCM)

# OUTLET -> GPIO
# Pi3 GPIO mapping
OUT1 = 14
OUT2 = 15
OUT3 = 18
OUT4 = 23
OUT5 = 24
OUT6 = 25
OUT7 = 8
OUT8 = 7

# PINS (Update each year based on outlet usage)
TREE = OUT1
SANTA_HOUSE = OUT2
POST_OFFICE = OUT4
ELVES_BUNK = OUT5
REINDEER_STABLES = OUT6
TRAIN = OUT7
C9 = OUT8
AMBIENT = OUT8


# Modes
ALL = 99
DISCO = 1337
WIZARDS = 7331
DUCK_DUCK_GOOSE = 7332
OFF = 7300
WARP_SPEED = 1338
WARP_REVERSE = 1339
ALT_BUILDINGS = 1340
SPEAKER_VIZ = 1341


# Input to Pins Dict
input_pin_dict = {
    'SANTA_HOUSE': SANTA_HOUSE,
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
    'OFF': OFF,
    'WARP_SPEED': WARP_SPEED,
    'WARP_REVERSE': WARP_REVERSE,
    'ALT_BUILDINGS': ALT_BUILDINGS,
    'SPEAKER_VIZ': SPEAKER_VIZ
    }

# in order left to right
PIN_LIST = [
    REINDEER_STABLES,
    ELVES_BUNK,
    TREE,
    SANTA_HOUSE,
    POST_OFFICE,
    C9,
    TRAIN
]

DISCO_PIN_LIST = PIN_LIST[:-1]
BUILDING_PIN_LIST = PIN_LIST[:-2]


class InvalidInputException(Exception):
    pass


def init_gpio():
    for i in PIN_LIST:
        GPIO.setup(i, GPIO.OUT)


def parse_input_to_pin(input_str):
    input_str = input_str.upper()

    if input_str not in input_pin_dict:
        raise InvalidInputException()

    print(input_str)
    return input_pin_dict[input_str]


def blink(delay=0.2):
    turn_on_all_relays()
    sleep(delay)
    turn_off_all_relays()


def duck_duck_goose():
    set_relay(C9)
    pins = BUILDING_PIN_LIST
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
        SANTA_HOUSE,
        TREE,
        ELVES_BUNK,
        REINDEER_STABLES,
        ELVES_BUNK,
        TREE,
        SANTA_HOUSE
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
    p4 = BUILDING_PIN_LIST[:4]
    piano_n(p4)


def piano9():
    p9 = [
        REINDEER_STABLES,
        ELVES_BUNK,
        TREE,
        SANTA_HOUSE,
        POST_OFFICE,
        # TODO: Should POST_OFFICE be twice? To mimic end and restart from end
        SANTA_HOUSE,
        TREE,
        ELVES_BUNK
    ]
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


def set_relays(pins=[]):
    for pin in pins:
        set_relay(pin)


def set_relay(pin):
    if pin == ALL:
        turn_on_all_relays()
        return

    if GPIO.input(pin) is None:
        print('pin {} is None'.format(pin))

    print(f"{pin} is {GPIO.input(pin)}")

    if GPIO.input(pin) == 1:
        GPIO.output(pin, GPIO.LOW)
        print(f"{pin} OFF")
    else:
        GPIO.output(pin, GPIO.HIGH)
        print(f"{pin} ON")


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
    for i in range(6):
        alt_back_forth() # 0:32
    blink()
    piano()
    print('0:38')
    for i in range(6):
        alt_back_forth() # 0:38
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
    blink()  # end 3:02

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

    for pin in BUILDING_PIN_LIST:
        sleep(delay)
        set_relay(pin)
        sleep(delay)

    turn_off_all_relays()
    sleep(0.1)
    turn_on_all_relays()
    sleep(0.5)


def alt_back_forth(delay=0.15):
    turn_off_all_relays()
    set_relay(C9)
    wizard_pins = BUILDING_PIN_LIST

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
    for pin in DISCO_PIN_LIST:
        GPIO.output(pin, GPIO.LOW)


def turn_on_all_relays():
    # use disco pin list to avoid rapid on/off of train
    for pin in DISCO_PIN_LIST:
        GPIO.output(pin, GPIO.HIGH)


def turn_on_all_village_lights():
    print("ALL VILLAGE ON")
    village_pin_list = BUILDING_PIN_LIST
    for pin in village_pin_list:
        GPIO.output(pin, GPIO.HIGH)


def disco_mode():
    count = 120
    while count > 0:
        r = randint(0, len(DISCO_PIN_LIST) - 1)
        pin = DISCO_PIN_LIST[r]
        set_relay(pin)
        count -= 1
        sleep(0.1)

    blink(0.5)
    sleep(0.5)
    blink(0.5)
    turn_on_all_relays()


def duck_duck_goose_st(delay=0.25):
    pins = DISCO_PIN_LIST
    for _ in range(4):
        for p in pins:
            sleep(delay)
            set_relay(p)
            sleep(delay)
            set_relay(p)


def speaker_viz(delay=0.25, repeat_num=5):
    turn_off_all_relays()
    sleep(delay)
    cmds = [
        [TREE],
        [SANTA_HOUSE, ELVES_BUNK],
        [SANTA_HOUSE, ELVES_BUNK],
        [TREE],
        [TREE],
        [SANTA_HOUSE, ELVES_BUNK],
        [POST_OFFICE, REINDEER_STABLES],
        [POST_OFFICE, REINDEER_STABLES],
        [SANTA_HOUSE, ELVES_BUNK],
        [TREE]
    ]

    for _ in range(repeat_num):
        for pins in cmds:
            set_relays(pins)
            sleep(delay)

    turn_on_all_relays()


def alternate_buildings(delay=0.25, repeat_num=10):
    left_mid_right = BUILDING_PIN_LIST[0], BUILDING_PIN_LIST[2], BUILDING_PIN_LIST[4]
    inner_two = BUILDING_PIN_LIST[1], BUILDING_PIN_LIST[3]

    turn_off_all_relays()
    sleep(delay)

    for _ in range(repeat_num):
        set_relays(left_mid_right)
        sleep(delay)
        set_relays(left_mid_right)
        sleep(delay)
        set_relays(inner_two)
        sleep(delay)
        set_relays(inner_two)
        sleep(delay)

    set_relays(left_mid_right)
    sleep(delay)
    set_relays(left_mid_right)
    sleep(delay)

    turn_on_all_relays()


def warp_viz(delay=0.05, repeat_num=10, reverse=False):
    cmds = [
        [BUILDING_PIN_LIST[2]],
        [BUILDING_PIN_LIST[1],BUILDING_PIN_LIST[3]],
        [BUILDING_PIN_LIST[0], BUILDING_PIN_LIST[4]],
        [BUILDING_PIN_LIST[2]],
        [BUILDING_PIN_LIST[1], BUILDING_PIN_LIST[3]],
        [BUILDING_PIN_LIST[0], BUILDING_PIN_LIST[4]],
    ]

    if reverse:
        cmds.reverse()

    turn_off_all_relays()
    sleep(delay)
    for _ in range(repeat_num):
        for pins in cmds:
            sleep(delay)
            set_relays(pins)
            sleep(delay)
    turn_on_all_relays()


def warp_viz_reverse(delay=0.05, repeat_num=10):
    warp_viz(delay, repeat_num, True)


def get_sqs():
    sqs = boto3.resource('sqs',
                         region_name='us-east-1',
                         aws_secret_access_key=os.getenv('AWS_SECRET', ''),
                         aws_access_key_id=os.getenv('AWS_KEY', ''),
                         use_ssl=True)
    queue = sqs.Queue(os.getenv('SQS_QUEUE', ''))
    return queue


def pick_random_action():
    funcs = [
        disco_mode,
        # wizards_main,
        duck_duck_goose,
        alternate_buildings,
        warp_viz,
        warp_viz_reverse,
        speaker_viz
    ]

    random_action = choice(funcs)

    print("Random action: " + str(random_action))
    random_action()


class SQSMessage(object):
    def __init__(self, message):
        self.message = message


def msg_object_hook(name, d):
    cls = {b'App\\Jobs\\ChristmasVillageJob': SQSMessage}[name]
    return cls(d[b'message'].decode())


def parse_sqs_msg(body):
    body = json.loads(body)
    en = body['data']['command'].encode()
    msg = ps.loads(en, object_hook=msg_object_hook)
    return msg


def main():
    pin_func_mapping = {
        WIZARDS: wizards_main,
        DISCO: disco_mode,
        DUCK_DUCK_GOOSE: duck_duck_goose_st,
        WARP_SPEED: warp_viz,
        WARP_REVERSE: warp_viz_reverse,
        ALT_BUILDINGS: alternate_buildings,
        SPEAKER_VIZ: speaker_viz,
        OFF: turn_off_all_relays
    }

    init_gpio()
    queue = get_sqs()

    max_time_before_random_action = 180
    pick_interaction_timer = 0
    current_sleep_duration = 1

    while True:
        sleep(current_sleep_duration)
        try:
            messages = queue.receive_messages()
        except Exception as ex:
            # set messages to empty list on sqs failure
            messages = list()
            print(ex)

        if pick_interaction_timer >= max_time_before_random_action:
            #pick_random_action()
            turn_on_all_village_lights()
            pick_interaction_timer = 0

        if len(messages) == 0:
            pick_interaction_timer += 1
            current_sleep_duration = 2
            continue
        else:
            current_sleep_duration = 0.5

        msg = messages[0]

        try:
            parsed_msg = parse_sqs_msg(msg.body)
            pin = parse_input_to_pin(parsed_msg.message)
        except InvalidInputException as ex:
            print(ex)
            msg.delete()
            continue

        try:
            msg.delete()
        except ClientError as ex:
            print("Caught Exception (ClientError)")
            print(ex)
        except Exception as ex:
            print("Default Caught Exception")
            print(ex)

        if pin in pin_func_mapping:
            pin_func_mapping[pin]()
        else:
            set_relay(pin)


if __name__ == '__main__':
    main()
