import socket

URL = "54.254.162.148"
PORT = 1337

encrypted = b';e\xc6\xd3\xb5\xed\xcaz\xd82\x97{`\x02\xd0\xee\xdf%\x18\xeaf\xaa/,\'3\xael\x83\xd9\xf2u\xda\'\xf5\xb0\xad"q\xfa\xf1\n\xecRZ?rh\x92{\x07\xaf@J4Y\xd2\x9a\xad9\xf0\xf4\x90\xf1'


def contact(cipherText):
    decryptedByteArray = []
    bytesInCipherText = len(cipherText)
    blocksOfCipherText = int(bytesInCipherText / 16)

    # connect to server
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((URL, PORT))

    # send your ciphertext (as bytes) to the Oracle
    conn.send(cipherText)
    serverResult = conn.recv(7)
    conn.close()

    return serverResult.decode('utf-8') == 'ree'


for i in range(255):
    e = []
    e.append(bytearray(encrypted[0:16]))
    e.append(bytearray(encrypted[16:32]))
    e.append(bytearray(encrypted[32:48]))

    try_cipher = []
    try_cipher.append(e[0])
    try_cipher.append(e[1])
    try_cipher.append(e[2])

    # try_cipher[1][5]  = 203
    # try_cipher[1][13] ^= 108 ^ 3
    try_cipher[1][10] ^= 45 ^ 6
    try_cipher[1][11] ^= 45^ 6
    try_cipher[1][12] ^= 102 ^ 6
    try_cipher[1][13] ^= 108 ^ 6
    try_cipher[1][14] ^= 97 ^ 6
    try_cipher[1][15] ^= 103 ^ 6



    if contact(bytes(try_cipher[0]) + bytes(try_cipher[1]) + bytes(try_cipher[2])):
        print(i)

print(try_cipher)




    # if contact(try_Bytes): print(i)
