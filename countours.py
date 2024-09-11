import cv2
import numpy as np


img=cv2.imread('image.png')

#cv2.imshow("photo",img)

blank=np.zeros(img.shape,dtype="uint8")
cv2.imshow("blank",blank)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray_image",gray)

blur=cv2.GaussianBlur(gray,(5,5),cv2.BORDER_DEFAULT)
cv2.imshow("blur",blur)


canny=cv2.Canny(blur,125,175)
cv2.imshow("canny",canny)

contours,hiererchies=cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
print(f"{len(contours)}")


cv2.drawContours(blank,contours,-1,(0,0,255),1)
cv2.imshow("countours",blank)

cv2.waitKey(0)
cv2.destroyAllWindows()
