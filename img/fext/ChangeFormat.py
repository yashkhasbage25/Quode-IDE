from PIL import Image
import os

pth = input("Paste the image: ")

format = input("Enter the desired format: ")

img = Image.open(pth)
img.convert('RGBA')
img.save(os.path.splitext(pth)[0]+'.'+format)
