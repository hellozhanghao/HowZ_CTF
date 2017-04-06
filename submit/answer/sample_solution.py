import time

from submit.answer.CFB import *

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

f = open("/Users/zhanghao/Desktop/Documents/Term7/Maps/HowZ_CTF/submit/HaoZ_Challenge/secret.pdf", 'rb')

input = f.read()

ba = bytearray(input)

f.close()

def append(digit, word):
    print(word)
    if digit == 0:
        key = hashlib.md5(word.encode('utf-8')).digest()
        plain = cfb_inv(ba, bytearray(key))
        text = str(plain)
        if text.find("%PDF-") != -1:
            print("Found PDF file with key: ",word)
            f = open("decrypted.pdf", 'wb')
            f.write(plain)
            f.close()
            print("Time taken: ", time.time() - start_time, "s")
            exit()

    else:
        for i in alphabet:
            append(digit - 1, word + i)


start_time = time.time()

append(3, '')
#
