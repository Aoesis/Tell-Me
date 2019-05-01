from num2words import num2words
from subprocess import call

cmd_beg='espeak -s100 '
cmd_end='| aplay /home/pi/Desktop/Text.wav 2>/dev/null'
cmd_out= '--stdout > /home/pi/Desktop/Text.wav'

##text = raw_input('enter the text: ')
##print (text)

text = 'Paracetamol'

call([cmd_beg+cmd_out+' ' +text+cmd_end], shell=True)