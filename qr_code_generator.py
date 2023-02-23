import qrcode

data = 'https://github.com/Rahul-Budhan'

img = qrcode.make(data)

img.save("<image_path>")