import numpy as np
import cv2

cv2.namedWindow("meme_window", cv2.WINDOW_NORMAL)
cv2.resizeWindow("meme_window", 500, 500)

image = cv2.imread("blinking_guy.jpg")
print(image.shape)

cv2.imshow("meme_window", image)
cv2.waitKey(0)