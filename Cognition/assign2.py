import numpy as np
import cv2

# //Convert to Grayscale//
image = cv2.imread("Week1_Images/Cat03.jpg")
grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)           # Gray image
# cv2.imshow("Original", image)
cv2.imshow("Grayscale", grayImg)


# //Draw concentric circle//
img = np.zeros((300, 300, 3), dtype = "uint8")
# cv2.imshow("Blank", img)

white = (255,255,255)

(centerX, centerY) = (img.shape[1]//2, img.shape[0]//2) # width, height
for r in range(0, 175, 25):
    cv2.circle(img, (centerX, centerY), r, white)

cv2.imshow("concentric circles", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# // Mask //
mask2 = np.zeros(grayImg.shape[:2], dtype="uint8")
cv2.circle(img=mask2, center= (grayImg.shape[0] // 2, grayImg.shape[1] // 2), radius=150, color=(220), thickness=-1)
masked = cv2.bitwise_and(grayImg, grayImg, mask=mask2)
cv2.imshow("Masked", masked)
cv2.waitKey(0)
