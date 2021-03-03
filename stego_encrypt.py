#!C:\Python33\python.exe
  
import binascii
from Crypto.Cipher import AES
from Crypto import Random
import hashlib
  
secretFile = input('Enter secret file name: ')
carrierFile = input('Enter carrier file name: ')
fileOut = input('Enter output file name: ')
 
password = input('Enter the key: ').encode('utf-8')
key = hashlib.sha256(password).digest()
 
IV = Random.new().read(AES.block_size)
secretSig = IV
print('IV: ', binascii.hexlify(IV).decode('utf-8'))
 
mode = AES.MODE_CBC
encryptor = AES.new(key, mode, IV=IV)
  
with open(secretFile, 'rb') as s: #secretfile
    secretData = s.read()
     
    if len(secretData) % 16 != 0: #pad with spaces if too small
        secretData += bytes(([0x20]) * (16 - len(secretData) % 16))
         
    secretData = encryptor.encrypt(secretData)    
     
with open(carrierFile, 'rb') as c: #carrier
    carrierData = c.read()
  
target = open(fileOut, 'wb')
target.write(carrierData)
target.write(secretSig)
target.write(secretData)
target.close()
 
pause = input('File done. Press enter.')
