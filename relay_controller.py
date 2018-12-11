import boto3
from time import sleep
import RPi.GPIO as GPIO
from random import randint

GPIO.setmode(GPIO.BCM)

# PINS
SANTA_HOUSE = 2
ELVES_BUNK = 3
POST_OFFICE = 4
REINDEER_STABLES = 17
TREE = 27
TRAIN = 22

# Modes
ALL = 99
DISCO = 1337

# pin_list = [2, 3, 4, 17, 27, 22, 10, 9]

pin_list = [
    SANTA_HOUSE,
    ELVES_BUNK,
    POST_OFFICE,
    REINDEER_STABLES,
    TREE,
    TRAIN,
    10,
    9
]


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
        return ALL
    elif input == 'DISCO':
        return DISCO


def set_relay(pin):
    if pin == ALL:
        for p in pin_list:
            GPIO.output(p, GPIO.HIGH)

    if GPIO.input(pin) is 1:
        GPIO.output(pin, GPIO.LOW)
    else:
        GPIO.output(pin, GPIO.HIGH)


def disco_mode():
    count = 120
    while count > 0:
        r = randint(0, len(pin_list))
        pin = pin_list[r]
        set_relay(pin)
        count -= 1


def get_sqs():
    sqs = boto3.resource('sqs',
                            region_name='',
                            aws_secret_access_key='',
                            aws_access_key_id='',
                            use_ssl=True)
    queue = sqs.Queue('')
    return queue


def main():
    queue = get_sqs()

    while True:
        sleep(15)
        msg = queue.receive_messages()[0]
        pin = parse_input_to_pin(msg['body'])
        if pin == DISCO:
            disco_mode()
        else:
            set_relay(pin)
        queue.delete_message(ReceiptHandle=msg['_receiptHandle'])


if __name__ == '__main__':
    main()
