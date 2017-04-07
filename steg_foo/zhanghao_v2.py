from PIL import Image
import numpy as np
import pprint
import sys

pp = pprint.PrettyPrinter(indent=5)

np.set_printoptions(threshold=sys.maxsize)

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


for i in range(len(red)):
    for j in range(len(red[0])):
        red[i][j] = red[i][j] & 0b11




data = np.array(red)
data = data.astype(np.int8)
print(data)

#Rescale to 0-255 and convert to uint8

im = Image.new()
im.save('test.png')

