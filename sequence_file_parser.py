import os.path
# import sys
# import fake_rpi
#
# sys.modules['RPi'] = fake_rpi.RPi
# sys.modules['RPi.GPIO'] = fake_rpi.RPi.GPIO

# import RPi.GPIO


SLEEP = "SLEEP"
ON = "ON"
OFF = "OFF"
START_LOOP = "START_LOOP"
END_LOOP = "END_LOOP"

PIN_ON = 1 #GPIO.HIGH
PIN_OFF = 0 #GPIO.LOW


class SequenceFileParser:

    def __init__(self):
        self._valid_pins = ["TREE", "SANTA_HOUSE", "POST_OFFICE", "ELVES_BUNK", "REINDEER_STABLES", "TRAIN", "C9"]
        self._valid_cmds = [SLEEP, ON, OFF, START_LOOP, END_LOOP]

    def parse_file(self, input_path: str, output_path: str=None):
        if output_path is None:
            output_path = os.path.join("sequences/", os.path.basename(input_path))
            output_path = output_path.replace(".txt", ".py")
            print(output_path)

        outfile_ptr = open(output_path, 'w')

        indent = ""
        file_ptr = open(input_path)
        for line in file_ptr:
            line = line.upper()
            if line == '\n' or '#' in line:
                continue

            args = line.strip().split(" ")
            cmd = args[0]

            if cmd not in self._valid_cmds:
                print(f"Error: Invalid command '{cmd}'")
                exit()

            if cmd == SLEEP:
                value = args[1]
                print(f"{cmd}: {value}")
                outfile_ptr.write(f"{indent}sleep({value})\n")
            elif cmd == ON or cmd == OFF:
                pins = args[1:]
                on_off_val = PIN_ON if cmd == ON else PIN_OFF
                print(f"{cmd}: {pins}")
                for pin in pins:
                    outfile_ptr.write(f"{indent}GPIO.out({pin}, {on_off_val})\n")
            elif cmd == START_LOOP:
                indent = " "*4
                count = args[1]
                outfile_ptr.write(f"for _ in range({count}):\n")
                print("START LOOPING...")
            elif cmd == END_LOOP:
                indent = ""
                print("END LOOPING...")

        outfile_ptr.close()


if __name__ == "__main__":
    parser = SequenceFileParser()
    parser.parse_file("community_sequences/deck_the_halls_war_pig.txt")
