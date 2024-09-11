import cv2

img=cv2.imread("image.png")


color=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
color_2=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

cv2.imshow("image",color)
cv2.imshow("image_2",color_2)


cv2.waitKey(0)