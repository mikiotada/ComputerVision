import argparse
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

ap = argparse.ArgumentParser(description="Load, display, and save an image")
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# store the arguments in dic
image = cv2.imread(args["image"])
print(f"w: {image.shape[1]} pixels | h: {image.shape[0]} pixels | channels: {image.shape[2]}")

# show an image
# cv2.imshow("Image", image)
# cv2.waitKey(0)

plt.figure()
f, axarr = plt.subplots(1, 2)
# convert image from BGR to RGB
axarr[0].imshow(image)
axarr[1].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

# save an image
# cv2.imwrite("image.jpg", image)
