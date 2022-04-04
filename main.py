import json
from PIL import Image

image = Image.new('RGB', (2000, 2000))

with open("orders.json") as file:
    order = json.load(file)

for x, y, color in order[0]:
    image.putpixel((x, y), (255, 0, 0))

image.save("img.png")