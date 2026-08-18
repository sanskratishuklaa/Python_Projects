import qrcode

img = qrcode.make("https://www.linkedin.com/in/sanidhya-pathak-53b984378")
img.save("linkedIn_qr.png")

print("QR Code Generated Successfully!")