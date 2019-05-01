#!/usr/bin/python

# para que este scritp sea ejecutable:
# sudo chmod +x nombreDelArchivo.py

import RPi.GPIO as GPIO
import os
import time
import sys
import bluetooth
import serial 

#notas: posible boton de reinicio, contar para un else en (1) donde se salga del while true

#from time import time,sleep,asctime,localtime
bs=serial.Serial("/dev/rfcomm0",baudrate=9600)

#Sockets para bluetooth
#BTsock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#BTsock.connect(("98:D3:33:80:D7:F2",1))


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

	#try:
	#	data = BTsock.recv(1024)
	#	print(data)
	#except BlockingIOError:
	#	data =""
	
	try:
		#if GPIO.input(butPin): #not pressed
		#	contador = contador
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

