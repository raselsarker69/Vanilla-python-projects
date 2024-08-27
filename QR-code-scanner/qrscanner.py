import qrcode

from pyzbar.pyzbar import decode

from PIL import Image


myqr = qrcode.make("https://www.youtube.com/watch?v=J0Zqeqi0zQc")
myqr1 = qrcode.make("https://raselsarker11.github.io/Happy-shoping/")

myqr.save("myqr.png", scale = 8)
myqr1.save("myqr1.png", scale = 7)

a = decode(Image.open("myqr.png"))

print(a[0].data.decode("ascii"))