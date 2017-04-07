from PIL import Image
import pprint
import numpy
import sys
import string

pp = pprint.PrettyPrinter(indent=5)

numpy.set_printoptions(threshold=sys.maxsize)

image = Image.open("newredkey.png")
image = image.convert('RGB')

red = []

width, height = image.size
for x in range(height):
    red.append([])
    for y in range(width):
        r, g, b = image.getpixel((y, x))
        # print (r,g,b)
        red[x].append(r)


def a_print(arr, fill):
    for i in range(len(arr)):
        line = ''
        for j in range(len(arr[0])):
            line += str(arr[i][j]).zfill(fill) + ' '
        print(line)


print(len(string.printable))

cipher = []
for i in range(len(red)):
    cipher.append([])
    for j in range(len(red[0])):
        if red[i][j] in range(32,127) :
            # print(i)
            cipher[i].append(chr(red[i][j]))
        else:
            cipher[i].append(" ")

a_print(cipher, fill=1)


#
# 107, 111, 112, 105
# space = [ord('k'),ord('o'),ord('p'),ord('i')]
# print(space)
# for i in range(len(red)):
#     for j in range(len(red[0])):
#         if red[i][j] in space:
#             print(i,j, chr(red[i][j]), red[i][j])

# cipher =



# nice try!
# for key in range(255):
#     ans = bytearray()
#     buffer = -1
#     for i in range(len(red)):
#         for j in range(len(red[0])):
#             if red[i][j] != buffer:
#                 buffer = red[i][j]
#                 if buffer == key:
#                     ans.append(j%256)
#     print(ans)
