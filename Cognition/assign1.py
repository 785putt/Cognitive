import cv2 
import numpy as np

image = cv2.imread("C:/Users/mrput/Documents/VSProject/Cognition/Week1_Images/sunset_image.png")



# shapes = np.zeros_like(image, np.uint8)
# cv2.rectangle(shapes, (400, 15), (955, 175), (255, 255, 255), cv2.FILLED)
# out = image.copy()
# alpha = 0.5
# mask = shapes.astype(bool)
# out[mask] = cv2.addWeighted(image, alpha, shapes, 1 - alpha, 0)[mask]
# # cv2.imshow('Image', image)
# # cv2.imshow('Shapes', shapes)
# cv2.imshow('Output', out)

# cv2.waitKey(0)


overlay = image.copy()
# overlay1 = image.copy()

# 1
x, y, w, h = 400, 0, 400, 300  # Rectangle parameters
cv2.rectangle(overlay, (x, y), (x+w, y+h), (255, 0, 0), -1)  # A filled rectangle

# 2
x1, y1, w1, h1 = 400, 300, 400, 300  # Rectangle parameters
cv2.rectangle(overlay, (x1, y1), (x1+w1, y1+h1), (0, 0, 255), -1)  # A filled rectangle

# 3
x2, y2, w2, h2 = 0, 300, 400, 300  # Rectangle parameters
cv2.rectangle(overlay, (x2, y2), (x2+w2, y2+h2), (0, 255, 0), -1)  # A filled rectangle

alpha = 0.4  # Transparency factor.

# Following line overlays transparent rectangle
# over the image
image_new = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
# image_new1 = cv2.addWeighted(overlay1, alpha, image, 1 - alpha, 0)

cv2.imshow("some", image_new)

cv2.waitKey(0)

cv2.destroyAllWindows()




# height, width, channels = image.shape
# b, g, r = cv2.split(image)

# zeros = np.zeros((height, width,1), np.uint8)
# r = cv2.merge((r,zeros,zeros))
# g = cv2.merge((zeros,g,zeros))
# b = cv2.merge((zeros,zeros,b))

# image[0:int(height/2), int(width/2)::] = r[0:int(height/2), int(width/2)::]
# image[int(height/2)::, 0:int(width/2)] = g[int(height/2)::, 0:int(width/2)]
# image[int(height/2)::, int(width/2)::] = b[int(height/2)::, 0:int(width/2)]

# cv2.imshow('image', image)
# cv2.waitKey(0)