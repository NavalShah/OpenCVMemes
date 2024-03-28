import numpy as np
import cv2

cv2.namedWindow("meme_window", cv2.WINDOW_NORMAL)
cv2.resizeWindow("meme_window", 1000, 500)

image = cv2.imread("blinking_guy.jpg")
print(image.shape)


#adding text: cv2.putText(image, text, (x, y), font, font_scale, color, line_thickness)
cv2.putText(image, "Shrek.", (50, 500), cv2.FONT_HERSHEY_SIMPLEX, 5, (0,0,0), 15)
cv2.putText(image, "Shrek.", (50, 500), cv2.FONT_HERSHEY_SIMPLEX, 5, (255,255,255), 7)

image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)



cv2.imshow("meme_window", image)
cv2.waitKey(0)

question = input("Do you wan to save your image? ")
if question.lower() == "yes":
    name=input("name you meme") + ".jpg"
    cv2.imwrite(name, image)