from PIL import Image
import os

pth = input("Paste the image: ")

height = int(input("Height: "))
width = int(input("Width: "))
head, tail = os.path.split(pth)
img = Image.open(pth)
new_img = img.resize((width, height), Image.ANTIALIAS)
new_img.save(head+"/_"+tail)
