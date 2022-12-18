from pygame import mixer
from gtts import gTTS
import os
import subprocess

#Instantiate mixer
mixer.init()

#Load audio file
lang = input("which language? we have.. en, fr, es:  ")
mytext = input("what should i say?:  ")

myobj = gTTS(text=mytext, lang=lang, slow=False)
myobj.save("test.mp3")

mixer.music.load("test.mp3")

print("sound started playing....")

#Set preferred volume
mixer.music.set_volume(10.0)

#Play the music
mixer.music.play()

#Infinite loop
while True:
	print("------------------------------------------------------------------------------------")
	print("Press 'p' to pause the music")
	print("Press 'r' to resume the music")
	print("Press 'e' to exit the program")

	#take user input
	userInput = input(" ")
	
	if userInput == 'p':

		# Pause the music
		mixer.music.pause()	
		print("sound is paused....")
	elif userInput == 'r':

		# Resume the music
		mixer.music.unpause()
		print("sound is resumed....")
	elif userInput == 'e':

		# Stop the music playback
		mixer.music.stop()
		print("sound is stopped....")
		save = input("do u want to save the audiofile? y/n ")
		if save != "y":
			subprocess.run(['rm', "test.mp3"], stdout=subprocess.PIPE)
			break
		else:
			name = input("give me a name for the audiofile: ")
			subprocess.run(['mv', "test.mp3", name+".mp3"], stdout=subprocess.PIPE)
			break
