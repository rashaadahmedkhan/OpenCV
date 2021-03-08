#basic introduction and rotating image from webcam.
import cv2

img = cv2.imread('assets/pic1-desert.jpg', -1)
# -1 cv2.IMREAD_COLOR - loads a colour image.
# 0 cv2.IMREAD_GREYSCALE - loads image in greyscale
# 1 cv2.IMREAD_UNCHANGED - loads image as such including alpha channel

#resize image
img = cv2.resize(img, (0, 0), fx=0.1, fy=0.1)

#rotate
img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite('pic1v2.jpg', img)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()