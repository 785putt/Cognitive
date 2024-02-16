import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("Week3_Images/Coin.png")



def sobel_filter(img):
    # Define the Sobel kernels for x and y direction
    kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    kernel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    
    # Pad the image with zeros to handle edge pixels
    padded_img = np.pad(img, ((1, 1), (1, 1)), 'constant')
    
    # Get the dimensions of the padded image
    height, width = padded_img.shape
    
    # Create an array to store the gradient magnitude
    grad = np.zeros_like(img)
    
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            # Apply the x and y Sobel kernels to the current pixel
            grad_x = (kernel_x * padded_img[y-1:y+2, x-1:x+2]).sum()
            grad_y = (kernel_y * padded_img[y-1:y+2, x-1:x+2]).sum()
            
            # Compute the gradient magnitude
            grad[y-1, x-1] = np.sqrt(grad_x**2 + grad_y**2)
    
    return grad

img = cv2.imread("Week3_Images/Coin.png", cv2.IMREAD_GRAYSCALE)

# Apply the Sobel filter
gradient = sobel_filter(img)
cv2.imshow('Non libraly Sobel filter', gradient)    




# Drawing contour
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# apply binary thresholding
ret, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
# visualize the binary image
# cv2.imshow('Binary image', thresh)
# cv2.imwrite('image_thres1.jpg', thresh)

# detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

# draw contours on the original image
image_copy = image.copy()
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(255, 0, 0), thickness=2, lineType=cv2.LINE_AA)              
# see the results
cv2.imshow('Draw contour on image', image_copy)
cv2.imwrite('contours_none_image1.jpg', image_copy)

image2 = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Blurred", image2)

canny = cv2.Canny(image, 240, 250)  # 50, 150
cv2.imshow("Canny", canny)

# cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
# cv2.imshow('Contours', image)

print("coins in the image : ", len(contours))
cv2.waitKey(0)