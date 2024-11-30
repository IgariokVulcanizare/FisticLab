import random
from PIL import Image
mc=0
im = Image.open("PSA/danger_zone.png")

n=int(input("Enter the number of points(more the better the precise): "))
x_max,y_max=im.size
red_threshold ,green_threshold ,blue_threshold = im.getpixel((2,2))[:3]


for a in range(n):
    x = random.randint(0,x_max-1)
    y = random.randint(0,y_max-1)
    r, g, b = im.getpixel((x, y))[:3]

    if (r != red_threshold) or (g != green_threshold) or (b != blue_threshold):
        mc+=1
print("Area is equal to = ", (mc/n)*42)