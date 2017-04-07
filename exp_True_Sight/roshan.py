import hashlib

salt = "!@#$%"

f = open("wordlist", "r")

wordlist = []

hash_ans = "17f03d8d940e0947cbb380fedad3140c55dae9d7"
print(hash_ans)

word = f.readline()
while word != "":
    wordlist.append(word[:-1])
    word = f.readline()

for word_1 in wordlist:
    for word_2 in wordlist:
        message = salt + word_1 + word_2
        digest = hashlib.sha1(message.encode("utf-8")).hexdigest()
        if digest == hash_ans:
            print(message)
