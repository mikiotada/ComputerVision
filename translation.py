# translation is the shifting of an image along the x and y axis.

import numpy as np
import matplotlib.pyplot as plt
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i",
                "--image",
                required=True,
                help="Path to the image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])


translation_M = np.float32([[1, 0, -50],  # shift the image left by 50 pixels (negative for left, positive for right)
                            [0, 1, -90]])  # shift the image up by 90 pixels (negative for up, positive for down)
shifted_up_left = cv2.warpAffine(img,
                                 translation_M,
                                 (img.shape[1], img.shape[0]))


translation_M = np.float32([[1, 0, 50],  # shift the image right by 50 pixels (negative for left, positive for right)
                            [0, 1, 90]])  # shift the image down by 90 pixels (negative for up, positive for down)
shifted_down_right = cv2.warpAffine(img,
                                    translation_M,
                                    (img.shape[1], img.shape[0]))  # (width, height)


plt.figure()
f, axarr = plt.subplots(1, 4)
# convert image from BGR to RGB
axarr[0].set_title("Original")
axarr[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

axarr[1].set_title("Shifted \n Up and Left")
axarr[1].imshow(cv2.cvtColor(shifted_up_left, cv2.COLOR_BGR2RGB))

axarr[2].set_title("Shifted \n Down and Right")
axarr[2].imshow(cv2.cvtColor(shifted_down_right, cv2.COLOR_BGR2RGB))

# use own translation function
shifted = imutils.translate(img, 0, 100)  # shift the image down by 100
axarr[3].set_title("Shifted \n Down")
axarr[3].imshow(cv2.cvtColor(shifted, cv2.COLOR_BGR2RGB))

plt.show()
