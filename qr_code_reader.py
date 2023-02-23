from pyzbar.pyzbar import decode
from PIL import Image   

img = Image.open("<image_path>")

result = decode(img)

for obj in result:
    print(obj.data)
    print(obj.type)