import cv2
import pandas as pd

image=cv2.imread("image.png")


#averaging

average=cv2.blur(image,(6,6))
cv2.imshow("image",average)

#gaussian blur

gaussian_blur=cv2.GaussianBlur(image,(7,7),0)
cv2.imshow("image",gaussian_blur)

#median blur
median=cv2.medianBlur(image,3)
cv2.imshow("median",median)



bilateral=cv2.bilateralFilter(image,5,35,25)
cv2.imshow("bilateral",bilateral)





cv2.waitKey(0)