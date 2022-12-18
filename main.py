import RPi.GPIO as GPIO
import time
import random
import os
import pygame
import logging
from random import randint


def play_sound(audio_file, vol=100.0):
    pygame.mixer.init()
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

# log testing
logging.basicConfig(filename='/home/pi/Desktop/door/example.log', 
			level=logging.DEBUG, format= '%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    			datefmt='%Y-%m-%d %H:%M:%S',)


music_dir = "/home/pi/Desktop/door/audio_files/"
all_mp3 = [os.path.join(music_dir, f)
           for f in os.listdir(music_dir) if f.endswith('.mp3')]

logging.info('working dir: ' + str(os.getcwd()))

DOOR_SENSOR_PIN = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

isOpen = False
oldIsOpen = False

while True:
    oldIsOpen = isOpen
    isOpen = GPIO.input(DOOR_SENSOR_PIN) == False
    # only play sound if door opens
    if (isOpen != oldIsOpen and isOpen):
        logging.info('Change detected: play sound')
        song = random.choice(all_mp3)
        logging.info(str(song))
        play_sound(song)
#     else:
#         time.sleep(0.5)
#         print('No change')
    elif GPIO.input(18):
#        logging.info("Closed")
        time.sleep(0.5)

    elif GPIO.input(18) == False:
#        print("Open")
        time.sleep(0.5)
