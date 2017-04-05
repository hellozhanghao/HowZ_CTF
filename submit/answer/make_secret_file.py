from submit.answer.CFB import *
import hashlib

key = "ITA"

in_file = open('plain.pdf', 'rb')
f = in_file.read()

result = cfb(bytearray(f), bytearray(hashlib.md5(key.encode("utf-8")).digest()))
test = open('secret.pdf', 'wb')
test.write(result)
