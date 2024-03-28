import numpy as np
import cv2

cv2.namedWindow("meme_window", cv2.WINDOW_NORMAL)
cv2.resizeWindow("meme_window", 1000, 500)

image = cv2.imread("blinking_guy.jpg")
print(image.shape)

cv2.putText(image, "THIS iS MEMEE Text", (50, 500), cv2.FONT_HERSHEY_SIMPLEX, 5, (0,0,0), 15)
cv2.putText(image, "THIS iS MEMEE Text", (50, 500), cv2.FONT_HERSHEY_SIMPLEX, 5, (255,255,255), 7)



cv2.imshow("meme_window", image)
cv2.waitKey(0)