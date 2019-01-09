import boto3
from time import sleep
import RPi.GPIO as GPIO
from random import randint

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
ELVES_BUNK = OUT2
POST_OFFICE = OUT4
REINDEER_STABLES = OUT1
TREE = OUT5
TRAIN = OUT7

# Modes
ALL = 99
DISCO = 1337
WIZARDS = 7331

# pin_list = [2, 3, 4, 17, 27, 22, 10, 9]

pin_list = [
    SANTA_HOUSE,
    ELVES_BUNK,
    POST_OFFICE,
    REINDEER_STABLES,
    TREE,
    TRAIN
]

disco_pin_list = pin_list[:-1]


class InvalidInputException(Exception):
    pass


def init_gpio():
    for i in pin_list:
        GPIO.setup(i, GPIO.OUT)


def parse_input_to_pin(input):
    if input == 'SANTA_HOUSE':
        print('SANTA_HOUSE')
        return SANTA_HOUSE
    elif input == 'SANTA_HOUSE':
        print('SANTA_HOUSE')
        return SANTA_HOUSE
    elif input == 'ELVES_BUNK':
        print('ELVES_BUNK')
        return ELVES_BUNK
    elif input == 'POST_OFFICE':
        print('POST_OFFICE')
        return POST_OFFICE
    elif input == 'REINDEER_STABLES':
        print('REINDEER_STABLES')
        return REINDEER_STABLES
    elif input == 'TREE':
        print('TREE')
        return TREE
    elif input == 'TRAIN':
        print('TRAIN')
        return TRAIN
    elif input == 'ALL':
        print('ALL')
        return ALL
    elif input == 'DISCO':
        print('DISCO')
        return DISCO
    elif input == 'WIZARDS':
        print('WIZARDS')
        return WIZARDS
    else:
        raise InvalidInputException()


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
    alt_back_forth(delay=0.3)
    for i in range(4): alt_back_forth()
    turn_off_all_relays()
    sleep(0.1)
    turn_on_all_relays()
    for i in range(4): alt_back_forth()

    turn_on_all_relays()

def triple_beat():
    turn_off_all_relays()

    sleep(0.1)
    turn_on_all_relays()
    sleep(0.1)
    turn_off_all_relays()
    sleep(0.1)
    turn_on_all_relays()
    sleep(0.1)
    turn_off_all_relays()
    sleep(0.1)
    turn_on_all_relays()
    sleep(0.3)

def piano():
    turn_off_all_relays()

    sleep(0.2)
    set_relay(ELVES_BUNK)
    sleep(0.2)
    set_relay(REINDEER_STABLES)
    sleep(0.2)
    set_relay(SANTA_HOUSE)
    sleep(0.2)
    set_relay(TREE)
    sleep(0.2)
    set_relay(POST_OFFICE)
    sleep(0.2)

    turn_off_all_relays()
    sleep(0.1)
    turn_on_all_relays()
    sleep(0.5)

def alt_back_forth(delay=0.15):
    turn_off_all_relays()

    wizard_pins = [ELVES_BUNK, REINDEER_STABLES, SANTA_HOUSE, TREE, POST_OFFICE]

    for pin in wizard_pins:
        set_relay(pin)
        sleep(0.15)
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

def get_sqs():
    sqs = boto3.resource('sqs',
                         region_name='',
                         aws_secret_access_key='',
                         aws_access_key_id='',
                         use_ssl=True)
    queue = sqs.Queue('')
    return queue


def main():
    init_gpio()
    queue = get_sqs()

    while True:
        sleep(3)
        messages = queue.receive_messages()

        if len(messages) == 0:
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
        else:
            set_relay(pin)



if __name__ == '__main__':
    main()
