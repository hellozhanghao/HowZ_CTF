import hashlib
#Group: HowZ
#Draft code

plaintext = 'something'
data = bytearray()
data.extend(map(ord,plaintext))

fullround = 80

keyplain = 'test'
hash1 = hashlib.md5(keyplain.encode('utf-8'))  #Generate 128 bits key
keyarray = bytearray(hash1.digest())

ivplain = 'hello'
hash2 = hashlib.md5(ivplain.encode('utf-8'))  #Generate 128 bits iv
iv = bytearray(hash2.digest())


def getrounds(data, roundnumber, keyarray, iv):
    state = iv
    for i in range(roundnumber):
        roundarray = simplifiedAES(keyarray, iv)
        statearray = xor(roundarray, data)

    return statearray



def simplifiedAES(keyarray):
    #TO DO
    #implement simplified AES encryption method
    #return encryptedResult
    

def xor(roundarray, data):
    statearray = bytearray()
    for i in range(len(roundarray)):
        statearray.append(roundarray[i]^data[i])
    return statearray


statearray = getrounds(data, fullround, keyarray, iv)
ciphertext = ""
for i in statearray:
    ciphertext+=chr(i)  #generate ciphertext
print(ciphertext)

#decryption: replace data with ciphertext
result = getrounds(statearray, fullround, keyarray, iv)
plaintext = ""
for i in result:
    plaintext+=chr(i)
print(plaintext)


