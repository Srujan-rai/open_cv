import cv2

cap=cv2.VideoCapture(0)

while True:
    success,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.putText(frame,"i myself srujan",(100,100),1,cv2.FONT_HERSHEY_PLAIN ,(255,255,255),2)
    cv2.imshow("gray",gray)
    cv2.imshow("image",frame)
    cv2.waitKey(1)
    
cv2.destroyAllWindows()