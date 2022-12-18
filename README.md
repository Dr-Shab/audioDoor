# The Raspberry Welcome: Automated Home Audio Greetings

A nice little gadget to welcome you or any guests when entering your home with a snippet from your favourite song or any kind of sound.

## Requirements **_NOTE_** Adopted from alexus37/hg2gDoor

Let me first share my shopping list required for this project. First, you need a [Raspberry Pi 3 b+](https://www.amazon.com/ELEMENT-Element14-Raspberry-Pi-Motherboard/dp/B07P4LSDYV) (overkill, but I had one laying around) and a [door sensor switch](https://pixelelectric.com/mc-38-wired-door-sensor-switch/) to be able to determine if the door is open or not. Additionally, you need some kind of speaker. I wanted to try out this [one](https://www.monkmakes.com/pi_speaker_kit/), but I guess any speaker that has an AUX cord will do.

## Wiring

The wiring is super easy and does not require any soldering. In my case, I needed to connect my speaker to the 5V and to the ground. To be able to use my code directly connect the door sensor to the Raspberry pin 18 and that's it.

## Connect and deploy

Connect to the PI via ssh and clone the repository. In my case the name of the Pi is galaxy.

```bash
    ssh pi@galaxy.local
	git clone git@github.com:alexus37/hg2gDoor.git
```

## Code overview

The whole code required is basically in the file `main.py` and it loads all the audio samples (different sighs for more variety) and uses pygame to play them if the door state changes.

## Autostart

If you want to add the script to the autostart folder run:

```bash
    crontab -e
```

and add the following lines

`@reboot python3 /home/pi/hg2gDoor/main.py >>/home/pi/log.txt 2>&1 &`
