import mediapipe as mp 
import cv2

cap=cv2.VideoCapture(0)
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils

while True:
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    #print(results)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            print(handLms)
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
            
    cv2.imshow("image",img)
    cv2.waitKey(1)
    
cv2.destroyAllWindows()
cap.release()