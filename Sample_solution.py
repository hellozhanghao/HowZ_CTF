import hashlib
import time

alphabet = 'abcdefghijklmnopqrstuvwxyz'

f = open("topsecret.pdf", 'rb')
cipher = f.read()
print(cipher)
f.close()


#todo main funtion to be implemeted
def SAES_CFB(data, key):

    # return result
    pass


def append(digit, word):
    if digit == 0:
        key = hashlib.md5(word.encode('ascii')).hexdigest()
        plain = SAES_CFB(cipher, key)
        if plain.find("%PDF-") != -1:
            print("Found PDF file with key: ", key)
            f = open("decrypt.pdf", 'wb')
            f.write(plain)
            f.close()

    else:
        for i in alphabet:
            append(digit - 1, word + i)


start_time = time.time()

append(5, '')

print("Time taken: ", time.time() - start_time, "s")
