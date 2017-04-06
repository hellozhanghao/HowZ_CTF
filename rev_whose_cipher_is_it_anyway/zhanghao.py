import string
import requests
import random
import pprint

pp= pprint.PrettyPrinter(indent=5)


print(string.printable)
plain="                                                                               "
mask ="0000000000000000000000000000000000000000000000000000000000000000000000000000000"

frequency = []
for i in range(79):
    frequency.append({})

cipher_ans = "rz@{o ?IH/cXZFaQs?F8web,ZwnKFP&|wx{gv|'?{V@A*:nqFkTbNCHy<1gwlb<'Dgp`G\"NU_d/WeD^"

# key = []
#
# plain_1 = "a"*79
# cipher_1 = "}s<3aC&cVG6xtN\"^+KFbxC1xH1:(p#?H]hcs?j~IWMA\$:^R:dnR8(JR}/ %+W~2eidqUKM1HM&&iYE"
# # print(plain)
# for i in range(len(plain_1)):
#     key.append(string.printable.find(cipher_1[i])-string.printable.find(plain_1[i]))
# print(key)
#
# for i in range(len(plain_1)):
#     plain += string.printable[string.printable.find(cipher[i])+key[i]]
#
# print(plain)


def replace(text,char, pos):
    return text[:pos] + char + text[pos+1:]

url = "http://54.255.148.164"

def cipher(plain):
    data = dict(text=plain)

    # request = urllib.request.Request(url)
    # response = urllib.request.urlopen(request,timeout=3)
    r = requests.post(url, data=data, allow_redirects=True)
    content = r.text
    tag = content.find("Cipher Text :")
    tag2 = content.find("</h4>")
    return content[tag+len("Cipher Text : "):tag2]



while mask!=""









