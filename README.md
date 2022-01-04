# [ChristmasVillage.io](https://christmasvillage.io) Relay Controller

<img src="https://christmasvillage.io/images/christmas-village.jpg" height="350" alt="Raspberry Pi Christmas Village"/>

### Links
[ChristmasVillage.io - Live Stream & Controls](https://christmasvillage.io)  
[Youtube](https://www.youtube.com/channel/UC7OXhPt69vX3VBtggBRphAg)  
[Instagram](https://instagram.com/christmasvillage.io)

### About
This repository controls the light relays of the Christmas Village & Trains. The `relay_controller.py` runs on the raspberry pi.

### Setup
* Create a virtual environment in the repo folder:`virtualenv -p python3 venv`
* Activate virtualenv
  * Linux & Mac: `source venv/bin/activate`
  * Windows: `source venv/Scripts/activate`
* Install dependencies `pip install -r requirements.txt`

### Create a Custom Sequence
To create a custom sequence create a git branch for your work, then you can create a Pull Request (PR) to merge it into the repo.

Look at the `community_sequences/example_sequence.txt` to see a simple example of how to create a light show sequence.

Valid sequence commands: `ON, OFF, SLEEP, START_LOOP, END_LOOP`  
Valid Pins/Lights: `TREE, SANTA_HOUSE, POST_OFFICE, ELVES_BUNK, REINDEER_STABLES, TRAIN, C9`  

Basic example to turn on and off the TREE light
```
ON TREE
SLEEP 1
OFF TREE
SLEEP 1
```

Turn multiple pins/lights on or off:
```
ON TREE SANTA_HOUSE POST_OFFICE
SLEEP 2
OFF TREE SANTA_HOUSE POST_OFFICE
SLEEP 1
```

Loop example:
```
START_LOOP 10
    ON TREE
    SLEEP 0.25
    OFF TREE
    SLEEP 0.25
END_LOOP
```
