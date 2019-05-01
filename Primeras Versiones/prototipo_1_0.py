#!/usr/bin/python

# para que este scritp sea ejecutable:
# sudo chmod +x nombreDelArchivo.py

import RPi.GPIO as GPIO
import os
import time
import sys
import bluetooth
import serial 


bs=serial.Serial("/dev/rfcomm0",baudrate=9600)

#Pin definitions for GPIO
butPin = 17

#variables
contador = 0
command = ""

#Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(butPin,GPIO.IN, pull_up_down=GPIO.PUD_UP)
time.sleep(1)
print "Comienza programa"

while True:

	
	try:
		
		a = str(bs.read())
		print a
		if a != "1" :
			contador = contador
		else:
			command = "fswebcam -S 20 -r 1280x720 -f 5 --set brightness=50%  --no-banner  /home/pi/Desktop/fotosCamara/"+str(contador)+".jpg"
			os.system(command)
			#time.sleep(1)
			contador = contador +1
	except  KeyboardInterrupt:
		BTsock.close()
		break

