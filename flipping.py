import argparse
import numpy as np
import matplotlib.pyplot as plt
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])

plt.figure()
f, axarr = plt.subplots(2, 2)

axarr[0][0].set_title("Original")
axarr[0][0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

# positive => around y-axis
flipped = cv2.flip(img, 1)
axarr[0][1].set_title("Flip around Y-axis")
axarr[0][1].imshow(cv2.cvtColor(flipped, cv2.COLOR_BGR2RGB))

# positive => around x-axis
flipped = cv2.flip(img, 0)
axarr[1][0].set_title("Flip around X-axis")
axarr[1][0].imshow(cv2.cvtColor(flipped, cv2.COLOR_BGR2RGB))

# positive => around x and y-axis
flipped = cv2.flip(img, -1)
axarr[1][1].set_title("Flip around X and Y-axis")
axarr[1][1].imshow(cv2.cvtColor(flipped, cv2.COLOR_BGR2RGB))

plt.show()
