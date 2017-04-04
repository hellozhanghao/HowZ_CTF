import hashlib

digest = hashlib.md5("hello".encode('ascii')).hexdigest()

print(digest)
b = bytes(digest, encoding='ascii')
print(b)

print(b[0])


ans = 1
for number in b :
    ans += number

print(ans)