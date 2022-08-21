import cv2
import mediapipe as mp

camera = cv2.VideoCapture(0)
mp_hands=mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.5)
tipid=[8,12,16,20]
def drawlandmarks(image,handLandmarks):
    if(handLandmarks):
        for i in handLandmarks:
            mp_drawing.draw_landmarks(image,i,mp_hands.HAND_CONNECTIONS)
def count_fingers(image,handLandmarks,handnumber=0):
    if(handLandmarks):
        landmarks=handLandmarks[handnumber].landmark
        fingers=[]
        for id in tipid:
            fingertipy = landmarks[id].y
            fingerbottomy=landmarks[id-2].y
            if(fingertipy<fingerbottomy):
                fingers.append(1)
            elif(fingertipy>fingerbottomy):
                fingers.append(0)
        if(landmarks[8].x>landmarks[12].x):
            fingertipx = landmarks[4].x
            fingerbottomx=landmarks[2].x
            if(fingertipx>fingerbottomx):
                fingers.append(1)
            elif(fingertipx<fingerbottomx):
                fingers.append(0)
        elif(landmarks[8].x<landmarks[12].x):
            fingertipx = landmarks[4].x
            fingerbottomx=landmarks[2].x
            if(fingertipx<fingerbottomx):
                fingers.append(1)
            elif(fingertipx>fingerbottomx):
                fingers.append(0)
        total_fingers=fingers.count(1)
        text=f'Fingers:{total_fingers}'
        cv2.putText(image,text,(100,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),5)
while True:
    ret,image=camera.read()
    results=hands.process(image)
    handLandmarks= results.multi_hand_landmarks
    drawlandmarks(image,handLandmarks)
    count_fingers(image,handLandmarks)
    cv2.imshow('result',image)
    if(cv2.waitKey(1)==32):
        break
cv2.destroyAllWindows()