import argparse
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

plt.figure()
f, axarr = plt.subplots(1, 2)

# cv2 store RGB pixels in reverse order
# When access each element in the tuple, need to view them in BGR order.
(b, g, r) = image[90, 490]
print(f"Pixel at (90, 490) | Red: {r} | Green: {g} | Blue: {b}")
axarr[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

image[90:600, 490:510] = (224, 119, 85)  # (b, g, r)
(b, g, r) = image[90, 490]
print(f"Pixel at (90, 490) | Red: {r} | Green: {g} | Blue: {b}")
axarr[1].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.show()
