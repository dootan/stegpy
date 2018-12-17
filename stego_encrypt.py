#!/bin/usr/python

import binascii
import base64

textFile = raw_input('Enter embeded file name: ')
imgFile = raw_input('Enter host file name: ')
secretSig = binascii.a2b_hex('FFFF0000FFFF0000FFFF')

fileOut = raw_input('Enter output file name: ')

with open(textFile, 'rb') as txt:
	content = txt.read()
	content = base64.b64encode(content)
	content = binascii.hexlify(content).upper()
	content = binascii.a2b_hex(content)
	#print content

#print 'Secret signature',secretSig
	
with open(imgFile, 'rb') as img:
	imageData = img.read()
	imageData = binascii.hexlify(imageData).upper()
	imageData = binascii.a2b_hex(imageData)
	#print imageData

target = open(fileOut, 'wb')
target.write(imageData)
target.write(secretSig)
target.write(content)
target.close()

##content = binascii.unhexlify(content)
##content = base64.b64decode(content)
##print ('content decoded: '),content

pause = raw_input('File done. Press enter.')
