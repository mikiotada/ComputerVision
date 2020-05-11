import numpy as np
import argparse
import imutils
import cv2
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])

plt.figure()
f, axarr = plt.subplots(1, 4)

axarr[0].set_title("Original")
axarr[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

# compute the new ratio of height and width
# ratio of new width vs old width
ratio = 150.0 / img.shape[1]
# width*height
dim = (150, int(img.shape[0]*ratio))

# INTER_LINEAR, INTER_CUBIC, INTER_NEAREST
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
axarr[1].set_title("Resized (Width=150)")
axarr[1].imshow(cv2.cvtColor(resized, cv2.COLOR_BGR2RGB))


ratio = 50./img.shape[0]
# width*height
dim = (int(img.shape[1]*ratio), 50)

resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
axarr[2].set_title("Resized (Height=50)")
axarr[2].imshow(cv2.cvtColor(resized, cv2.COLOR_BGR2RGB))


resized = imutils.resize(img, height=10)
axarr[3].set_title("Resized (height=10)")
axarr[3].imshow(cv2.cvtColor(resized, cv2.COLOR_BGR2RGB))


plt.show()
