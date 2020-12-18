guitar_sleep = 0.1
# GPIO.output(ALL, GPIO.HIGH)
# TURN ON ALL
GPIO.output(C9, GPIO.LOW)
GPIO.output(POST_OFFICE, GPIO.LOW)
GPIO.output(SANTA_HOUSE, GPIO.LOW)
GPIO.output(TREE, GPIO.LOW)
GPIO.output(ELVES_BUNK, GPIO.LOW)
GPIO.output(REINDEER_STABLES, GPIO.LOW)

# riff down
GPIO.output(POST_OFFICE , GPIO.HIGH)
sleep(rift_sleep)
GPIO.output(SANTA_HOUSE, GPIO.HIGH)
sleep(rift_sleep)
GPIO.output(TREE, GPIO.HIGH)
sleep(rift_sleep)
GPIO.output(ELVES_BUNK, GPIO.HIGH)
sleep(rift_sleep)
GPIO.output(REINDEER_STABLES, GPIO.HIGH)
sleep(rift_sleep)

# riff up
GPIO.output(REINDEER_STABLES, GPIO.LOW)
sleep(rift_sleep)
GPIO.output(ELVES_BUNK, GPIO.LOW)
sleep(rift_sleep)
GPIO.output(TREE, GPIO.LOW)
sleep(rift_sleep)
GPIO.output(SANTA_HOUSE, GPIO.LOW)
sleep(rift_sleep)
GPIO.output(POST_OFFICE, GPIO.LOW)
sleep(rift_sleep)

# lyrics background symbol | 0:01 - 0:05
for _ in range(50):
    GPIO.output(C9, GPIO.LOW)
    sleep(0.1)
    GPIO.output(C9, GPIO.HIGH)
    sleep(0.1)

# riff down
GPIO.output(POST_OFFICE , GPIO.HIGH)
sleep(rift_sleep)
GPIO.output(SANTA_HOUSE, GPIO.HIGH)
sleep(rift_sleep)
GPIO.output(TREE, GPIO.HIGH)
sleep(rift_sleep)
GPIO.output(ELVES_BUNK, GPIO.HIGH)
sleep(rift_sleep)
GPIO.output(REINDEER_STABLES, GPIO.HIGH)
sleep(rift_sleep)

# riff up
GPIO.output(REINDEER_STABLES, GPIO.LOW)
sleep(rift_sleep)
GPIO.output(ELVES_BUNK, GPIO.LOW)
sleep(rift_sleep)
GPIO.output(TREE, GPIO.LOW)
sleep(rift_sleep)
GPIO.output(SANTA_HOUSE, GPIO.LOW)
sleep(rift_sleep)
GPIO.output(POST_OFFICE, GPIO.LOW)
sleep(rift_sleep)

# lyrics background symbol  | 0:06 - 0:10
for _ in range(50):
    GPIO.output(C9, GPIO.LOW)
    sleep(0.1)
    GPIO.output(C9, GPIO.HIGH)
    sleep(0.1)

# riff down
GPIO.output(POST_OFFICE , GPIO.HIGH)
sleep(rift_sleep)
GPIO.output(SANTA_HOUSE, GPIO.HIGH)
sleep(rift_sleep)
GPIO.output(TREE, GPIO.HIGH)
sleep(rift_sleep)
GPIO.output(ELVES_BUNK, GPIO.HIGH)
sleep(rift_sleep)
GPIO.output(REINDEER_STABLES, GPIO.HIGH)
sleep(rift_sleep)

# riff up
GPIO.output(REINDEER_STABLES, GPIO.LOW)
sleep(rift_sleep)
GPIO.output(ELVES_BUNK, GPIO.LOW)
sleep(rift_sleep)
GPIO.output(TREE, GPIO.LOW)
sleep(rift_sleep)
GPIO.output(SANTA_HOUSE, GPIO.LOW)
sleep(rift_sleep)
GPIO.output(POST_OFFICE, GPIO.LOW)
sleep(rift_sleep)

# lyrics background symbol  | 0:11 - 0:16
for _ in range(50):
    GPIO.output(C9, GPIO.LOW)
    sleep(0.1)
    GPIO.output(C9, GPIO.HIGH)
    sleep(0.1)

# riff down
GPIO.output(POST_OFFICE , GPIO.HIGH)
sleep(rift_sleep)
GPIO.output(SANTA_HOUSE, GPIO.HIGH)
sleep(rift_sleep)
GPIO.output(TREE, GPIO.HIGH)
sleep(rift_sleep)
GPIO.output(ELVES_BUNK, GPIO.HIGH)
sleep(rift_sleep)
GPIO.output(REINDEER_STABLES, GPIO.HIGH)

# riff up
GPIO.output(REINDEER_STABLES, GPIO.LOW)
sleep(rift_sleep)
GPIO.output(ELVES_BUNK, GPIO.LOW)
sleep(rift_sleep)
GPIO.output(TREE, GPIO.LOW)
sleep(rift_sleep)
GPIO.output(SANTA_HOUSE, GPIO.LOW)
sleep(rift_sleep)
GPIO.output(POST_OFFICE, GPIO.LOW)
sleep(rift_sleep)
sleep(rift_sleep)