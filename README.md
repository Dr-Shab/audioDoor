# The Raspberry Welcome: Automated Home Audio Greetings

A nice little gadget to welcome you or any guests when entering your home with a snippet from your favourite song or any kind of sound.  
  
**_NOTE:_** Requirements, Wiring, etc. adopted from [alexus37/hg2gDoor](https://github.com/alexus37/hg2gDoor) with some additions.

## Requirements 

Let me first share my shopping list required for this project. First, you need a [Raspberry Pi 3 b+](https://www.amazon.com/ELEMENT-Element14-Raspberry-Pi-Motherboard/dp/B07P4LSDYV) (or any Raspberry with an audio jack or bluetooth capability) and a [door sensor switch](https://pixelelectric.com/mc-38-wired-door-sensor-switch/) to be able to determine if the door is open or not. Additionally, you need some kind of speaker. I wanted to try out this [one](https://www.monkmakes.com/pi_speaker_kit/), but I guess any speaker that has an AUX cord will do. If you plan to connect via bluetooth either your speaker supports it or you need an addiotional bluetooth adapter, which is then connected via AUX to the speaker.

## Wiring

The wiring is super easy and does not require any soldering. In my case, I needed to connect my speaker to the 5V and to the ground. To be able to use my code directly connect the door sensor to the Raspberry pin 18 and that's it.

## Connect and deploy

Connect to the PI via ssh and clone the repository. In my case the name of the Pi is galaxy.

    ssh pi@galaxy.local
    git clone https://github.com/Dr-Shab/audioDoor.git


## Code overview

The whole code required is basically in the file `main.py` and it loads all the audio samples (different sighs for more variety) and uses pygame to play them if the door state changes.

## Autostart

If you want to add the script to the autostart folder run:

`crontab -e`

and add the following lines

`@reboot python3 /home/pi/audioDoor/main.py 2>&1 &`
