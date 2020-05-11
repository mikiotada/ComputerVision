import numpy as np
import matplotlib.pyplot as plt
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])

plt.figure()
f, axarr = plt.subplots(1, 2)

axarr[0].set_title("Original")
axarr[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

cropped = img[50:550, 100:550]
axarr[1].set_title("Cropped")
axarr[1].imshow(cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB))

plt.show()
