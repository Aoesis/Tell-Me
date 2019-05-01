import binascii
with open('Imagen.txt', 'r') as myfile:
    data = myfile.read()
data=data.strip()
data=data.replace(' ', '')
data=data.replace('\n', '')
data=data.replace('&', '')
data=data.replace('#', '')
data = binascii.a2b_hex(data)
with open('imagenchidori.jpg', 'wb') as image_file:
    image_file.write(data)
