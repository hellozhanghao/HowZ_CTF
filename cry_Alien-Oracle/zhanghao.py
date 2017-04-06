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

    return serverResult.decode('utf-8')=='ree'


for i in range(255):
    e = []
    e.append(bytearray(encrypted[0:16]))
    e.append(bytearray(encrypted[16:32]))
    e.append(bytearray(encrypted[32:48]))

    try_cipher = []
    try_cipher.append(e[0])
    try_cipher.append(e[1])
    try_cipher.append(e[2])


    try_cipher[1][5]  = 203
    try_cipher[1][6]  = 93
    try_cipher[1][7]  = 71
    try_cipher[1][8]  = 90
    try_cipher[1][9]  = 15
    try_cipher[1][10] = 131
    try_cipher[1][11] = 65
    try_cipher[1][12] = 229
    try_cipher[1][13] = 181
    try_cipher[1][14] = 147
    try_cipher[1][15] = 18

    for j in range(5,16):
        try_cipher[1][j] ^= 11





    try_Bytes = bytes(try_cipher[0]) + bytes(try_cipher[1]) + bytes(try_cipher[2])
    if contact(try_Bytes): print(i)





