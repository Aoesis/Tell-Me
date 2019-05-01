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

#variables
contador = 0
command = ""


print ("Comienza programa")

##while True:
##
##        try:
##        ##Esperar a que se reciba el inicio del JPEG
##                a = str(bs.read(size=4))
##                print a
##                if a == "FFD8" :
##            ##Se recibe el inicio del JPEG
##            ##Crear archivo de la imagen.
##                    archivoImagen=open("Imagen.txt", "a+")
##            ##Escribir el contenido de la imagen
##                    while (a != "FFD9"):
##                    ##Add the rest of the image.
##                        archivoImagen.write(a)
##                        a = str(bs.read(size=4))
##                else:
##			##No se hace nada.
##        except  KeyboardInterrupt:
##                    break

buff = ""
while True:
	
	try:
		a = bs.read()
		print (a)
		if a == "&" :
			print("ya entre")
                        contador = 0
                        #archivoImagen=open("Imagen.txt", "w")
                        while (a != "#"):
                               contador = contador + 1
                               #archivoImagen.write(a)
                               #archivoImagen.write('\n')
			       buff += a
                               a= bs.read()
			       print (contador)
                        print ('ya')
                        print(contador)
                        contador = 0
                        #print (a);
			archivoImagen=open("Imagen.txt", "w")
			archivoImagen.write(buff)
                        archivoImagen.close()
			break;
		else:
			print("")
	except  KeyboardInterrupt:
		print ("except")
		break
