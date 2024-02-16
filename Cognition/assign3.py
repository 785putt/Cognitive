import cv2
# img = cv2.imread("Week3_Images/Coin.png", cv2.IMREAD_GRAYSCALE)
# # img = cv2.imread("Week3_Images/fingerprint.png", cv2.IMREAD_GRAYSCALE)
# cv2.imshow("input image", img)
# retval, segmentedImg = cv2.threshold(img, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# print("Otsu's threshold = ", retval)
# cv2.imshow("segmented image", segmentedImg)
# cv2.waitKey()
# cv2.destroyAllWindows()

import numpy as np
img = cv2.imread("Week3_Images/Coin.png", cv2.IMREAD_GRAYSCALE)
# cv2.imshow("input image", img)

retval, segmentedImg = cv2.threshold(img, 0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print("Otsu's threshold = ", retval)
cv2.imshow("THRESH_BINARY", segmentedImg)
cv2.waitKey()

# blurred = cv2.GaussianBlur(img, (5, 5), 0)
# thresh = cv2.adaptiveThreshold(blurred, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
# cv2.imshow("Mean Thresh", thresh)
# cv2.waitKey()

retval, segmentedImg = cv2.threshold(img, 0,255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU) 
cv2.imshow("THRESH_BINARY_INV", segmentedImg)
cv2.waitKey()

# retval, segmentedImg = cv2.threshold(img, 0,255, cv2.THRESH_TRUNC | cv2.THRESH_OTSU) 
# cv2.imshow("THRESH_TRUNC", segmentedImg)

# retval, segmentedImg = cv2.threshold(img, 0,255, cv2.THRESH_TOZERO | cv2.THRESH_OTSU)
# cv2.imshow("THRESH_TOZERO", segmentedImg)

# retval, segmentedImg = cv2.threshold(img, 0,255, cv2.THRESH_TOZERO_INV | cv2.THRESH_OTSU) 
# cv2.imshow("THRESH_TOZERO_INV", segmentedImg)
# cv2.waitKey()
cv2.destroyAllWindows()