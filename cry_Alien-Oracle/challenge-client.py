#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Team reyonnnnnnnnnnnnnnnnnnnn


import socket


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

if __name__ == "__main__":
    URL = "54.254.162.148"
    PORT = 1337

    encrypted = b';e\xc6\xd3\xb5\xed\xcaz\xd82\x97{`\x02\xd0\xee\xdf%\x18\xeaf\xaa/,\'3\xael\x83\xd9\xf2u\xda\'\xf5\xb0\xad"q\xfa\xf1\n\xecRZ?rh\x92{\x07\xaf@J4Y\xd2\x9a\xad9\xf0\xf4\x90\xf1'

    test = b'12345678901234567890123456789012345678901234567h\x92{\x07\xaf@J4Y\xd2\x9a\xad9\xf0\xf4\x90\xf1'

    # plain =



    # todo add by Zhang Hao, test
    cipherText = b'yeewfl'


    print(contact(test))






# Tip: The oracle only accepts bytes as input! One way to modify the byte string is:
# mutatedByte = (encrypted[15] ^ encrypted[16] ^ 0x1).to_bytes(1, 'little')
#
# modifiedCipherText = encrypted[0:15] + mutatedByte + encrypted[16:]
#
# This will allow you to modify individual bytes of the ciphertext.
# GLHF
