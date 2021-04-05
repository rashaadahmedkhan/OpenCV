# object detection

import numpy as np
import cv2

img = cv2.resize(cv2.imread('assets/game.jfif', 0), (0, 0), fx = 0.75, fy = 0.75)
template = cv2.resize(cv2.imread('assets/ball.jpg', 0), (0, 0), fx = 0.75, fy = 0.75)
h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
	img2 = img.copy()

	result = cv2.matchTemplate(img2, template, method)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
	print(min_loc, max_loc)
	if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
		location = min_loc
	else:
		location = max_loc

	bottom_right = (location[0] + w, location[1] + h)	
	cv2.rectangle(img2, location, bottom_right, 225, 5)
	cv2.imshow('Match', img2)
	cv2.waitKey(0)
	cv2.destroyAllWindows()