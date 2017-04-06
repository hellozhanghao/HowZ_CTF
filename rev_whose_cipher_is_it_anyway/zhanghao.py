import string
import requests
import random
import pprint

pp= pprint.PrettyPrinter(indent=5)

LEN = 79

print(string.printable)
plain="                                                                               "
mask ="0000000000000000000000000000000000000000000000000000000000000000000000000000000"

frequency = []
for i in range(79):
    frequency.append({})

cipher_ans = "rz@{o ?IH/cXZFaQs?F8web,ZwnKFP&|wx{gv|'?{V@A*:nqFkTbNCHy<1gwlb<'Dgp`G\"NU_d/WeD^"



def replace(text,char, pos):
    return text[:pos] + char + text[pos+1:]

url = "http://54.255.148.164"

def cipher(plain):
    data = dict(text=plain)

    # request = urllib.request.Request(url)
    # response = urllib.request.urlopen(request,timeout=3)
    r = requests.post(url, data=data, allow_redirects=True)
    content = r.text
    # print(content)
    tag = content.find("Cipher Text :")
    tag2 = content.find("</h4>")
    return content[tag+len("Cipher Text : "):tag2]



while mask!="1"* LEN:
    random_string = plain
    for i in range(LEN):
        if mask[i]=="0":
            random_string = replace(random_string, random.choice(string.printable),i)

    random_cipher = cipher(random_string)

    for i in range(LEN):
        if cipher_ans[i]==random_cipher[i]:
            plain=replace(plain,random_string[i],i)
            mask = replace(mask,"1",i)

    print(plain, mask, random_cipher)



# print(cipher("theKopiCTFflag=kopiCTF{Z2#2s81q"))










