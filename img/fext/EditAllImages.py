from PIL import Image
import os
import sys

filenames = [f for f in os.listdir('.') if os.path.isfile(f)]
format = input("Enter the desired format: ")

format = format.strip('.')
format = "." + format

height = int(input("Height: "))
width = int(input("Width: "))

if filenames is None:
    print("No image file in directory")

else:

    i = 0
    for filename in filenames:
        try:
            pth = filename
            img = Image.open(pth)
            img.convert('RGBA')
            new_img = img.resize((width, height), Image.ANTIALIAS)
            name, _ext = os.path.splitext(pth)
            new_img.save(name+format)

            i += 1
            img.close()

        except OSError:
            pass
            sys.exit()

        except ValueError:
            print("Unknown file extension:", format)

        finally:
            print("converted {} images".format(i))
