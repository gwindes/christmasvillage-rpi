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
OUTLETS = [OUT1, OUT2, OUT4, OUT5, OUT6, OUT7, OUT8]

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

PIN_MAP = {
    OUT1: "TREE",
    OUT2: "SANTA_HOUSE",
    OUT4: "POST_OFFICE",
    OUT5: "ELVES_BUNK",
    OUT6: "REINDEER_STABLES",
    OUT7: "TRAIN",
    OUT8: "C9"
}

DISCO_PIN_LIST = PIN_LIST[:-1]
BUILDING_PIN_LIST = PIN_LIST[:-2]


def init_gpio():
    for i in OUTLETS:
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



def set_relays(pins=[]):
    for pin in pins:
        set_relay(pin)


def set_relay(pin):
    if pin == ALL:
        turn_on_all_relays()
        return

    print(f"PIN: {pin}")

    if GPIO.input(pin) is None:
        print('pin {} is None'.format(pin))

    pin_state = "ON" if GPIO.input(pin) == 1 else "OFF"
    pin_name = PIN_MAP[pin]
    print(f"{pin_name} is {pin_state}")

    if GPIO.input(pin) == 1:
        GPIO.output(pin, GPIO.LOW)
        print(f"Set {pin_name} OFF")
    else:
        GPIO.output(pin, GPIO.HIGH)
        print(f"Set {pin_name} ON")


def turn_off_all_relays():
    # use disco pin list to avoid rapid on/off of train
    for pin in DISCO_PIN_LIST:
        GPIO.output(pin, GPIO.LOW)


def turn_on_all_relays():
    # use disco pin list to avoid rapid on/off of train
    print("TURN ON ALL")
    for pin in DISCO_PIN_LIST:
        pin_state = "ON" if GPIO.input(pin) == 1 else "OFF"
        pin_name = PIN_MAP[pin]
        print(f"{pin_name} is {pin_state}")
        GPIO.output(pin, GPIO.HIGH)


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


def main():
    init_gpio()
    turn_off_all_relays()

    while True:
        for pin in OUTLETS:
            print("="*25)
            sleep(0.025)
            set_relay(pin)
            sleep(0.025)
            set_relay(pin)


if __name__ == '__main__':
    main()
