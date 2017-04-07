from PIL import Image


image=Image.open("newredkey.png")
image=image.convert('RGB')

width, height = image.size
for x in range(height):
    for y in range(width):
        r, g, b = image.getpixel ((x,y))
        print (r,g,b)