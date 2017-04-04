import hashlib
import time

alphabet = 'abcdefghijklmnopqrstuvwxyz'

f = open("topsecret.pdf", 'rb')
input = f.read()

ba = bytearray(input)

f.close()


def byte_shift_cipher(data_in, key, mode):
    out = bytearray()

    for i in range(16):
        if mode == 'e':
            out.append((data_in[i] + key[i]) % 256)
        elif mode == 'd':
            out.append((data_in[i] - key[i]) % 256)
    return bytes(out)

def byte_xor(byte_1, byte_2):
    out = bytearray()
    for i in range(len(byte_1)):
        out.append(byte_1[i]^byte_2[i])
    return bytes(out)


# todo main funtion to be implemeted
def S_CFB(data, key, mode, IV=b'zaoZCTFisFUN!!23'):
    ba = bytearray(data)

    if mode == 'e':
        # add padding
        for i in range(16 - len(ba) % 16):
            ba.append(0)

    print(len(ba))

    # divide data into blocks
    in_blocks = []
    temp = bytearray()
    for i in range(len(ba)):
        temp.append(ba[i])
        if i % 16 == 15:
            in_blocks.append(temp)
            temp = bytearray()



    out_blocks = []

    for i in range(len(in_blocks)):
        if i !=0:
            temp = byte_shift_cipher(out_blocks[i - 1], key, mode=mode)
        else:
            temp = byte_shift_cipher(IV, key, mode=mode)
        out_blocks.append(byte_xor(temp, in_blocks[i]))

    out = bytearray()
    for byte in out_blocks:
        out += byte

    return bytes(out)


print(input)
cipher = S_CFB(data=input, key=hashlib.md5("hello".encode('utf-8')).digest(), mode='e')
print(cipher)
plain = S_CFB(data=cipher, key=hashlib.md5("hello".encode('utf-8')).digest(), mode='d')
print(plain)



def append(digit, word):
    if digit == 0:
        key = hashlib.md5(word.encode('ascii')).digest()
        plain = S_CFB(cipher, key,mode='d')
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
#
# print("Time taken: ", time.time() - start_time, "s")
