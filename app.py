import numpy as np
import cv2

#cv2.namedWindow("meme_window", cv2.WINDOW_NORMAL)
#cv2.resizeWindow("meme_window", 1000, 500)

#image = cv2.imread("blinking_guy.jpg")
#print(image.shape)




#adding text: cv2.putText(image, text, (x, y), font, font_scale, color, line_thickness)
#cv2.putText(image, "Shrek.", (50, 500), cv2.FONT_HERSHEY_SIMPLEX, 5, (0,0,0), 15)
#cv2.putText(image, "Shrek.", (50, 500), cv2.FONT_HERSHEY_SIMPLEX, 5, (255,255,255), 7)

#image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

#height,width,depth = image.shape

#for h in range(height):
#    for w in range(width):
#        for d in range(depth):
#            image[h, w, d] = image[h, w, d] -122


#cv2.imshow("meme_window", image)
#cv2.waitKey(0)

#question = input("Do you wan to save your image? ")
#if question.lower() == "yes":
#    name=input("name you meme") + ".jpg"
#    cv2.imwrite(name, image)
            

vc = cv2.VideoCapture(0)


#Escape with any key, makes stuff easier
while cv2.waitKey(1) < 0:
    hasFrame, frame = vc.read()
    frame = frame[100:-100, 130:-150]
    
    frame = cv2.resize(frame, (50, 50))

    height, width, depth = frame.shape

    for h in range(height):
        for w in range(width):
            for d in range(depth):
                frame[h, w, d] = 255-frame[h, w, d]

    frame = cv2.resize(frame, (500, 500), interpolation=cv2.INTER_NEAREST)
    cv2.putText(frame, "WHEN YOU MAKE MEMES IN PYTHON", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,0), 8)
    cv2.putText(frame, "WHEN YOU MAKE MEMES IN PYTHON", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255,255,255), 4)

    cv2.putText(frame, "IN PYTHON", (160, 475), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,0), 8)
    cv2.putText(frame, "IN PYTHON", (160, 475), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255,255,255), 4)

    cv2.imshow("window", frame)
    cv2.waitKey(1)

question = input("Do you want to save your image? ")
if question.lower() == "yes":
    name=input("name you meme") + ".jpg"
    cv2.imwrite(name, frame)

cv2.waitKey(0)
#Oh mah gawd no way it's this hard to use AI for opencv HAHUHHAHAa;ldjfa;ldkjfa;ldfskj
