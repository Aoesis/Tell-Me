#!/usr/bin/python

# para que este scritp sea ejecutable:
# sudo chmod +x nombreDelArchivo.py

import RPi.GPIO as GPIO
import os
import time
import sys
import bluetooth
import serial 
import subprocess
#notas: posible boton de reinicio, contar para un else en (1) donde se salga del while true

#subprocess.call(['python','BTconect.py'])
os.system("python BTconect.py &")
bs=serial.Serial("/dev/rfcomm0",baudrate=9600)


#variables
contador = 0
command = ""

command = "/home/pi/Desktop/proyecto/fotosCamara"
if os.path.exists(command): 
	command = "rm /home/pi/Desktop/proyecto/fotosCamara"
	os.system(command)
	command = "mkdir /home/pi/Desktop/proyecto/fotosCamara"
	os.system(command)
else:
	command = "mkdir /home/pi/Desktop/proyecto/fotosCamara"
	os.system(command)
	
time.sleep(1)
print "Comienza programa"

while True:
	
	try:
		a = str(bs.read())
		
		if a != "1" :
                        contador = contador
		else:
			time.sleep(2)
			command = "fswebcam -S 20 -r 1280x720 -f 5 --set brightness=50%  --no-banner  /home/pi/Desktop/fotosCamara/"+str(contador)+".jpg"
			os.system(command)
			contador = contador +1
	except  KeyboardInterrupt:
		print "except"
		break

