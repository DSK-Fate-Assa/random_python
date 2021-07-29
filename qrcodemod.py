import qrcode
import cv2

#encoding the qrcode
img = qrcode.make("https://github.com/DSK-Fate-Assa/random_python")
img.save("githublink.png")

#decoding the qrcode

d = cv2.QRCodeDetector() #renaming class
img1 = cv2.imread("githublink.png")
val, points, straightqrcode = d.detectAndDecode(img1)

print(val)
