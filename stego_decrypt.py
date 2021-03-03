#!C:\Python33\python.exe
 
import binascii
import hashlib
from Crypto.Cipher import AES
 
stegoFile = input('Enter the stego file name: ')
fileOut = input('Enter the output file name: ')
password = input('Enter the key: ').encode('utf-8')
IV = input('Enter the IV: ')
 
mode = AES.MODE_CBC
key = hashlib.sha256(password).digest()
 
IV = (binascii.hexlify(binascii.a2b_hex(IV)).upper())
sigLen = len(IV)
 
with open(stegoFile, 'rb') as s:
    content = s.read()
     
stegoData = (binascii.hexlify(content)).upper()
stegoLen = len(stegoData)
 
for i in range(0, len(stegoData)):
    if(stegoData[i:i+sigLen] == IV):    
        secretMsg = binascii.a2b_hex(stegoData[(i+sigLen):stegoLen])
         
        decryptor = AES.new(key, mode, IV=(binascii.a2b_hex(IV)))
        plain = decryptor.decrypt(secretMsg)
         
        target = open(fileOut, 'wb')
        target.write(plain)
        target.close()
        print(fileOut, 'file created.')
        input()
        break
