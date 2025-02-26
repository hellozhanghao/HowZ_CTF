import hashlib


def cfb(input_file, keyarray, iv=hashlib.md5("HAOZ".encode("utf-8")).digest()):
    vector = iv
    ciphertext = bytearray()
    blocknum = int(len(input_file) / 16)
    if len(input_file) % 16 != 0:
        blocknum += 1
    for i in range(len(input_file) % 16):
        input_file.append(0)
    for i in range(blocknum):
        cipherblock = getrounds(input_file[i * 16:i * 16 + 16], keyarray, vector)
        vector = cipherblock
        for k in cipherblock:
            ciphertext.append(k)
    return ciphertext


def cfb_inv(ciphertext, keyarray, iv=hashlib.md5("HAOZ".encode("utf-8")).digest()):
    vector = iv
    plaintext = bytearray()
    blocknum = int(len(ciphertext) / 16)
    for i in range(blocknum):
        plainblock = getrounds(ciphertext[i * 16:i * 16 + 16], keyarray, vector)
        vector = ciphertext[i * 16:i * 16 + 16]
        for k in plainblock:
            plaintext.append(k)
    return plaintext


def getrounds(block, keyarray, iv):
    cipherblock = bytearray()
    for i in range(len(block)):
        cipherbyte = shift_ascii(keyarray[i], iv[i])
        cipherblock.append(cipherbyte)
    cipherblock = xor(block, cipherblock)
    return cipherblock


def shift_ascii(key, vector):
    result = key + vector
    if result > 255:
        return result - 256
    return result


def xor(roundarray, data):
    statearray = bytearray()
    for i in range(len(roundarray)):
        statearray.append(roundarray[i] ^ data[i])
    return statearray
