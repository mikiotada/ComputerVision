import numpy as np
import cv2
import imutils
import argparse
import matplotlib.pyplot as plt


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])

plt.figure()
f, axarr = plt.subplots(1, 4)


axarr[0].set_title("Original")
axarr[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

# get the center (x,y) of the image
(h, w) = img.shape[:2]
center = (w//2, h//2)

M = cv2.getRotationMatrix2D(center, angle=45, scale=1.0)
rotated = cv2.warpAffine(img,
                         M,
                         (w, h))
# positve 45 degrees => the opposite of clockwise
axarr[1].set_title("Rotated \n by 45 Degrees")
axarr[1].imshow(cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB))


M = cv2.getRotationMatrix2D(center, angle=-90, scale=0.7)
rotated = cv2.warpAffine(img, M, (w, h))
# negative 90 degrees => the clockwise
axarr[2].set_title("Rotated \n by -90 Degrees \n and resized 0.7 scale")
axarr[2].imshow(cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB))

# use own rotate function
rotated = imutils.rotate(img, angle=180)
axarr[3].set_title("Rotated \n by 180 Degrees")
axarr[3].imshow(cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB))

plt.show()
