guitar_sleep = 0.1

GPIO.output(C9, GPIO.LOW)
GPIO.output(POST_OFFICE, GPIO.LOW)
GPIO.output(SANTA_HOUSE, GPIO.LOW)
GPIO.output(TREE, GPIO.LOW)
GPIO.output(ELVES_BUNK, GPIO.LOW)
GPIO.output(REINDEER_STABLES, GPIO.LOW)
sleep(0.1)

# riff down
GPIO.output(POST_OFFICE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(SANTA_HOUSE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(TREE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(ELVES_BUNK, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(REINDEER_STABLES, GPIO.HIGH)
sleep(guitar_sleep)

# riff up
GPIO.output(REINDEER_STABLES, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(ELVES_BUNK, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(TREE, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(SANTA_HOUSE, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(POST_OFFICE, GPIO.LOW)
sleep(guitar_sleep)


# lyrics background symbol | 0:01 - 0:05
for _ in range(50):
    GPIO.output(C9, GPIO.LOW)
    sleep(c9_sleep)
    GPIO.output(C9, GPIO.HIGH)
    sleep(c9_sleep)


# riff down
GPIO.output(POST_OFFICE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(SANTA_HOUSE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(TREE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(ELVES_BUNK, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(REINDEER_STABLES, GPIO.HIGH)
sleep(guitar_sleep)

# riff up
GPIO.output(REINDEER_STABLES, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(ELVES_BUNK, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(TREE, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(SANTA_HOUSE, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(POST_OFFICE, GPIO.LOW)
sleep(guitar_sleep)

# lyrics background symbol  | 0:06 - 0:10
for _ in range(50):
    GPIO.output(C9, GPIO.LOW)
    sleep(c9_sleep)
    GPIO.output(C9, GPIO.HIGH)
    sleep(c9_sleep)


# riff down
GPIO.output(POST_OFFICE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(SANTA_HOUSE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(TREE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(ELVES_BUNK, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(REINDEER_STABLES, GPIO.HIGH)
sleep(guitar_sleep)

# riff up
GPIO.output(REINDEER_STABLES, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(ELVES_BUNK, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(TREE, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(SANTA_HOUSE, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(POST_OFFICE, GPIO.LOW)
sleep(guitar_sleep)

# lyrics background symbol  | 0:11 - 0:16
for _ in range(50):
    GPIO.output(C9, GPIO.LOW)
    sleep(c9_sleep)
    GPIO.output(C9, GPIO.HIGH)
    sleep(c9_sleep)


# riff down
GPIO.output(POST_OFFICE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(SANTA_HOUSE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(TREE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(ELVES_BUNK, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(REINDEER_STABLES, GPIO.HIGH)
sleep(guitar_sleep)

# riff up
GPIO.output(REINDEER_STABLES, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(ELVES_BUNK, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(TREE, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(SANTA_HOUSE, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(POST_OFFICE, GPIO.LOW)
sleep(guitar_sleep)

# lyrics background symbol  | 0:17 - 0:21
for _ in range(50):
    GPIO.output(C9, GPIO.LOW)
    sleep(c9_sleep)
    GPIO.output(C9, GPIO.HIGH)
    sleep(c9_sleep)


# riff down
GPIO.output(POST_OFFICE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(SANTA_HOUSE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(TREE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(ELVES_BUNK, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(REINDEER_STABLES, GPIO.HIGH)
sleep(guitar_sleep)

# riff up
GPIO.output(REINDEER_STABLES, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(ELVES_BUNK, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(TREE, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(SANTA_HOUSE, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(POST_OFFICE, GPIO.LOW)
sleep(guitar_sleep)

# lyrics background symbol  | 0:22 - 0:26
for _ in range(50):
    GPIO.output(C9, GPIO.LOW)
    sleep(c9_sleep)
    GPIO.output(C9, GPIO.HIGH)
    sleep(c9_sleep)


# riff down
GPIO.output(POST_OFFICE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(SANTA_HOUSE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(TREE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(ELVES_BUNK, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(REINDEER_STABLES, GPIO.HIGH)
sleep(guitar_sleep)

# riff up
GPIO.output(REINDEER_STABLES, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(ELVES_BUNK, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(TREE, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(SANTA_HOUSE, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(POST_OFFICE, GPIO.LOW)
sleep(guitar_sleep)

# lyrics background symbol  | 0:27 - 0:31
for _ in range(40):
    GPIO.output(C9, GPIO.LOW)
    sleep(c9_sleep)
    GPIO.output(C9, GPIO.HIGH)
    sleep(c9_sleep)


# guitar twang :31-32
GPIO.output(POST_OFFICE, GPIO.HIGH)
sleep(0.05)
for _ in range(3):
    GPIO.output(SANTA_HOUSE, GPIO.HIGH)
    sleep(0.05)
    GPIO.output(TREE, GPIO.HIGH)
    sleep(0.05)
    GPIO.output(ELVES_BUNK, GPIO.HIGH)
    sleep(0.05)
    GPIO.output(ELVES_BUNK, GPIO.LOW)
    sleep(0.05)
    GPIO.output(TREE, GPIO.LOW)
    sleep(0.05)
    GPIO.output(SANTA_HOUSE, GPIO.LOW)
    sleep(0.05)

GPIO.output(POST_OFFICE, GPIO.LOW)
sleep(0.05)

# lyrics background symbol  | 0:31 - 0:32
for _ in range(10):
    GPIO.output(C9, GPIO.LOW)
    sleep(c9_sleep)
    GPIO.output(C9, GPIO.HIGH)
    sleep(c9_sleep)


# riff down
GPIO.output(POST_OFFICE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(SANTA_HOUSE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(TREE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(ELVES_BUNK, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(REINDEER_STABLES, GPIO.HIGH)
sleep(guitar_sleep)

# riff up
GPIO.output(REINDEER_STABLES, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(ELVES_BUNK, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(TREE, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(SANTA_HOUSE, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(POST_OFFICE, GPIO.LOW)
sleep(guitar_sleep)

# lyrics background symbol  | 0:33 - 0:35
for _ in range(20):
    GPIO.output(C9, GPIO.LOW)
    sleep(c9_sleep)
    GPIO.output(C9, GPIO.HIGH)
    sleep(c9_sleep)



# DRUM 1 2 1 3 1 2 4 4 5
GPIO.output(REINDEER_STABLES, GPIO.LOW)
sleep(0.1)
GPIO.output(REINDEER_STABLES, GPIO.HIGH)
sleep(0.1)
GPIO.output(ELVES_BUNK, GPIO.LOW)
sleep(0.1)
GPIO.output(ELVES_BUNK, GPIO.HIGH)
sleep(0.1)
GPIO.output(REINDEER_STABLES, GPIO.LOW)
sleep(0.1)
GPIO.output(REINDEER_STABLES, GPIO.HIGH)
sleep(0.1)
GPIO.output(TREE, GPIO.LOW)
sleep(0.1)
GPIO.output(TREE, GPIO.HIGH)
sleep(0.1)
GPIO.output(REINDEER_STABLES, GPIO.LOW)
sleep(0.1)
GPIO.output(REINDEER_STABLES, GPIO.HIGH)
sleep(0.1)
GPIO.output(ELVES_BUNK, GPIO.LOW)
sleep(0.1)
GPIO.output(ELVES_BUNK, GPIO.HIGH)
sleep(0.1)
GPIO.output(SANTA_HOUSE, GPIO.LOW)
sleep(0.1)
GPIO.output(SANTA_HOUSE, GPIO.HIGH)
sleep(0.1)
GPIO.output(SANTA_HOUSE, GPIO.LOW)
sleep(0.1)
GPIO.output(SANTA_HOUSE, GPIO.HIGH)
sleep(0.1)
GPIO.output(POST_OFFICE, GPIO.LOW)
sleep(0.1)
GPIO.output(POST_OFFICE, GPIO.HIGH)
sleep(0.1)


# lyrics background symbol  | 0:35 - 0:38
for _ in range(20):
    GPIO.output(C9, GPIO.LOW)
    sleep(c9_sleep)
    GPIO.output(C9, GPIO.HIGH)
    sleep(c9_sleep)


# riff down
GPIO.output(POST_OFFICE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(SANTA_HOUSE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(TREE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(ELVES_BUNK, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(REINDEER_STABLES, GPIO.HIGH)
sleep(guitar_sleep)

# riff up
GPIO.output(REINDEER_STABLES, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(ELVES_BUNK, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(TREE, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(SANTA_HOUSE, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(POST_OFFICE, GPIO.LOW)
sleep(guitar_sleep)

# lyrics background symbol  | 0:39 - 0:43
for _ in range(50):
    GPIO.output(C9, GPIO.LOW)
    sleep(c9_sleep)
    GPIO.output(C9, GPIO.HIGH)
    sleep(c9_sleep)


# riff down
GPIO.output(POST_OFFICE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(SANTA_HOUSE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(TREE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(ELVES_BUNK, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(REINDEER_STABLES, GPIO.HIGH)
sleep(guitar_sleep)

# riff up
GPIO.output(REINDEER_STABLES, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(ELVES_BUNK, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(TREE, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(SANTA_HOUSE, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(POST_OFFICE, GPIO.LOW)
sleep(guitar_sleep)

# lyrics background symbol  | 0:44 - 0:47
for _ in range(50):
    GPIO.output(C9, GPIO.LOW)
    sleep(c9_sleep)
    GPIO.output(C9, GPIO.HIGH)
    sleep(c9_sleep)


# riff down
GPIO.output(POST_OFFICE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(SANTA_HOUSE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(TREE, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(ELVES_BUNK, GPIO.HIGH)
sleep(guitar_sleep)
GPIO.output(REINDEER_STABLES, GPIO.HIGH)
sleep(guitar_sleep)

# riff up
GPIO.output(REINDEER_STABLES, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(ELVES_BUNK, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(TREE, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(SANTA_HOUSE, GPIO.LOW)
sleep(guitar_sleep)
GPIO.output(POST_OFFICE, GPIO.LOW)
sleep(guitar_sleep)

# guitar solo
GPIO.output(POST_OFFICE, GPIO.HIGH)
GPIO.output(SANTA_HOUSE, GPIO.HIGH)
GPIO.output(TREE, GPIO.HIGH)
GPIO.output(ELVES_BUNK, GPIO.HIGH)
GPIO.output(REINDEER_STABLES, GPIO.HIGH)
sleep(0.1)

GPIO.output(REINDEER_STABLES, GPIO.LOW)
sleep(0.1)
GPIO.output(REINDEER_STABLES, GPIO.HIGH)
sleep(0.1)


GPIO.output(REINDEER_STABLES, GPIO.LOW)
GPIO.output(ELVES_BUNK, GPIO.LOW)
sleep(0.1)
GPIO.output(REINDEER_STABLES, GPIO.HIGH)
GPIO.output(ELVES_BUNK, GPIO.HIGH)
sleep(0.1)


GPIO.output(REINDEER_STABLES, GPIO.LOW)
GPIO.output(ELVES_BUNK, GPIO.LOW)
GPIO.output(TREE, GPIO.LOW)
sleep(0.1)
GPIO.output(REINDEER_STABLES, GPIO.HIGH)
GPIO.output(ELVES_BUNK, GPIO.HIGH)
GPIO.output(TREE, GPIO.HIGH)
sleep(0.1)


for _ in range(5):
    GPIO.output(REINDEER_STABLES, GPIO.HIGH)
    GPIO.output(ELVES_BUNK, GPIO.HIGH)
    GPIO.output(TREE, GPIO.HIGH)
    sleep(0.02)
    GPIO.output(REINDEER_STABLES, GPIO.LOW)
    GPIO.output(ELVES_BUNK, GPIO.LOW)
    GPIO.output(TREE, GPIO.LOW)
    sleep(0.02)


GPIO.output(REINDEER_STABLES, GPIO.HIGH)
GPIO.output(ELVES_BUNK, GPIO.HIGH)
GPIO.output(TREE, GPIO.HIGH)
sleep(0.05)

# riff up
GPIO.output(REINDEER_STABLES, GPIO.LOW)
sleep(0.05)
GPIO.output(ELVES_BUNK, GPIO.LOW)
sleep(0.05)
GPIO.output(TREE, GPIO.LOW)
sleep(0.05)
GPIO.output(SANTA_HOUSE, GPIO.LOW)
sleep(0.05)
GPIO.output(POST_OFFICE, GPIO.LOW)
sleep(0.05)

# riff down
GPIO.output(POST_OFFICE, GPIO.HIGH)
sleep(0.05)
GPIO.output(SANTA_HOUSE, GPIO.HIGH)
sleep(0.05)
GPIO.output(TREE, GPIO.HIGH)
sleep(0.05)
GPIO.output(ELVES_BUNK, GPIO.HIGH)
sleep(0.05)
GPIO.output(REINDEER_STABLES, GPIO.HIGH)
sleep(0.05)

turn_on_all_relays()