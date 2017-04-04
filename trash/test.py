import hashlib


plaintext = 'hello world!!!!!'
data = bytearray()
data.extend(map(ord,plaintext))

fullround = 80
keyplain = 'test'
hash1 = hashlib.md5(keyplain.encode('utf-8'))
keyarray = bytearray(hash1.digest())

ivplain = 'hello'
hash2 = hashlib.md5(ivplain.encode('utf-8'))
iv = bytearray(hash2.digest())


def getrounds(data, roundnumber, keyarray, iv):
    state = iv
    for i in range(roundnumber):
        shiftkey = 1
        roundarray = shiftrounds(keyarray, shiftkey)
        statearray = xor(roundarray, data)
        state = statearray

    return statearray



def shiftrounds(keyarray, shiftkey):
    roundarray = bytearray()
    for bytes in keyarray:
        roundresult = bytes + shiftkey
        if roundresult > 255:
            roundresult-=256
        roundarray.append(roundresult)
    return roundarray

def xor(roundarray, data):
    statearray = bytearray()
    for i in range(len(roundarray)):
        statearray.append(roundarray[i]^data[i])
    return statearray



statearray = getrounds(data, fullround, keyarray, iv)
ciphertext = ""
for i in statearray:
    ciphertext+=chr(i)
print(ciphertext)

result = getrounds(statearray, fullround, keyarray, iv)
plaintext = ""
for i in result:
    plaintext+=chr(i)
print(plaintext)


