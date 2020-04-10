from PIL import Image
import os

for file in os.listdir("original"):
    if file.endswith(".png"):
        image_file = Image.open("original/" + file)
        image_file = image_file.convert("L")
        image_file.save("result/" + file[:-4] + "_grey.png")