import cv2

import numpy as np
img=cv2.imread("image.png")

blank=np.zeros(img.shape[:2],dtype="uint8")

b,g,r=cv2.split(img)

blue=cv2.merge([b,blank,blank])
green=cv2.merge([blank,g,blank])
red=cv2.merge([blank,blank,r])


cv2.imshow("blue",blue)
cv2.imshow("green",green)
cv2.imshow("red",red)






'''cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)'''



'''merged=cv2.merge([b,g,r])
cv2.imshow("merged",merged)'''
cv2.waitKey(0)

