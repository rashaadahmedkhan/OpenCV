# manipulating the image from the webcam.
import cv2
import random

img = cv2.imread('assets/pic1-desert.jpg', -1)

#resize image
#img = cv2.resize(img, (0, 0), fx=0.1, fy=0.1)

tag = img[500:700, 600:900]
img[100:300, 650:950] = tag

print(img[257][400])

for i in range(100):
	for j in range(img.shape[1]):
		img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()