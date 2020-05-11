import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")


red = (0, 0, 255)
for y in range(0, canvas.shape[0], 10):
    # when y = 0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280
    if (len(str(y)) == 1) or (len(str(y)) == 2 and int(str(y)[0]) % 2 == 0) or (len(str(y)) == 3 and int(str(y)[1]) % 2 == 0):
        for x in range(10, canvas.shape[1], 20):
            cv2.rectangle(canvas, (x, y), (x+9, y+9), red, -1)

    # when y = 10, 30, 50, 70, 90, 110, 130, 150, 170, 190, 210, 230, 250, 270, 290
    if (len(str(y)) == 2 and int(str(y)[0]) % 2 == 1) or (len(str(y)) == 3 and int(str(y)[1]) % 2 == 1):
        for x in range(0, canvas.shape[1], 20):
            cv2.rectangle(canvas, (x, y), (x+9, y+9), red, -1)


green = (0, 255, 0)
cv2.circle(canvas, (canvas.shape[1]//2, canvas.shape[0]//2), 50, green, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
