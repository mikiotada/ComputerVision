import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)

red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)

cv2.rectangle(canvas, (10, 10), (60, 60), green)

cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)

blue = (225, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)

(centerX, centerY) = (canvas.shape[1]//2, canvas.shape[0]//2)
white = (255, 255, 255)
for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white)

for i in range(0, 25):
    radius = np.random.randint(5, 200)
    color = np.random.randint(0, 256, size=(3,)).tolist()
    pt = np.random.randint(0, 300, size=(2,))
    cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
