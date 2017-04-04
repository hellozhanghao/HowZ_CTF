import hashlib
from saes import *

plaintext = 'hello world!!!!!1234567890123456'
data = bytearray()
data.extend(map(ord,plaintext))


keyplain = 'test'
hash1 = hashlib.md5(keyplain.encode('utf-8'))
keyarray = bytearray(hash1.digest())

ivplain = 'hello'
hash2 = hashlib.md5(ivplain.encode('utf-8'))
iv = bytearray(hash2.digest())

in_file = open('topsecret.pdf','rb')
f = in_file.read()

def cfb(input_file, keyarray, iv):
    vector = iv
    ciphertext = bytearray()
    blocknum = int(len(input_file)/16)
    if len(input_file)%16 != 0:
        blocknum+=1
    for i in range(len(input_file)%16):
        input_file.append(0)
    for i in range(blocknum):
        cipherblock = getrounds(input_file[i*16:i*16+16], keyarray, vector)
        vector = cipherblock
        for k in cipherblock:
            ciphertext.append(k)
    return ciphertext

def cfb_inv(ciphertext, keyarray, iv):
    vector = iv
    plaintext = bytearray()
    blocknum = int(len(ciphertext)/16)
    for i in range(blocknum):
        plainblock = getrounds(ciphertext[i*16:i*16+16], keyarray, vector)
        vector = ciphertext[i*16:i*16+16]
        for k in plainblock:
            plaintext.append(k)
    return plaintext
            

def getrounds(block, keyarray, iv):
    cipherblock = bytearray()
    for i in range(len(block)):
        cipherbyte = shift_ascii(keyarray[i],iv[i])
        cipherblock.append(cipherbyte)
    cipherblock = xor(block,cipherblock)
    return cipherblock
      


def shift_ascii(key, vector):
    result = key + vector
    if result>255:
        return result-256
    return result 

    

def xor(roundarray, data):
    statearray = bytearray()
    for i in range(len(roundarray)):
        statearray.append(roundarray[i]^data[i])
    return statearray

result = cfb(bytearray(f), keyarray, iv)
test = open('ciphered.pdf','wb')
test.write(result)

f2 = open('ciphered.pdf','rb')
f2 = f2.read()
result2 = cfb_inv(bytearray(f2), keyarray, iv)
test2 = open('plain.pdf','wb')
test2.write(result2)










