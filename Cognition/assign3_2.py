import cv2
import matplotlib.pyplot as plt
from skimage import data
# from skimage.filters import tall_threshold
import numpy as np
from skimage.filters import threshold_minimum
import matplotlib.image as mpimg

def threshold(img):
# img = cv2.imread("Week3_Images/Coin.png", cv2.IMREAD_GRAYSCALE)
    thresh_min = threshold_minimum(img)
    binary_min = img > thresh_min
    binary_max = img < thresh_min

    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    ax[0].imshow(binary_min, cmap=plt.cm.gray)
    ax[0].set_title('Thresholded (min)')

    ax[1].imshow(binary_max, cmap=plt.cm.gray)
    ax[1].set_title('Thresholded (idfk)')
    # for a in ax[:, 0]:
    #     a.axis('off')
    plt.show()


def rgb2gray(rgb):
    width = img.shape[1]
    height = img.shape[0]

    def thresholding(max):
        for item in range(height):
            for item2 in range(width):
                if img[item][item2] > max:
                    img[item][item2] = 255

                else:
                    img[item][item2] = 0

    thresholding(127)
    cv2.imshow("Image", img)
    cv2.waitKey(0)


if __name__=='__main__':
    img = cv2.imread("Week3_Images/Coin.png", cv2.IMREAD_GRAYSCALE)     
    # gray = rgb2gray(img)    
    # plt.imshow(gray, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
    # plt.show()
    rgb2gray(img)
