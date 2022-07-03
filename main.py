from storing import markIt
import cv2
import face_recognition
import numpy as np
import os

path = 'ImagesResources'
image = []
classNames = []
myList = os.listdir(path)
for cls in myList:
    curImg = cv2.imread(f'{path}/{cls}')
    image.append(curImg)
    classNames.append(os.path.splitext(cls)[0])

def encoding_finder(images):
    encoded_list = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoded_list.append(face_recognition.face_encodings(img)[0])
    return encoded_list

encoded_known = encoding_finder(image)
print('Encoding Completed')

cap = cv2.VideoCapture(0)
presence = False
loop = False


while True:
    success, img = cap.read()
    imgS  = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faces = face_recognition.face_locations(imgS)
    encodings = face_recognition.face_encodings(imgS, faces)

    for encode_faces, facesLoc in zip(encodings, faces):
        matches = face_recognition.compare_faces(encoded_known, encode_faces) 
        faceDis = face_recognition.face_distance(encoded_known, encode_faces)
        matchindex = np.argmin(faceDis) 

        if matches[matchindex]:
            name = classNames[matchindex].upper()
            presence=True
            prat = markIt(name, presence)
            print(prat)
            if prat == 'Attendance done':
                loop = True
            y1,x2,y2,x1 = facesLoc
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img, (x1, y2-35), (x2,y1), (0,255, 0), 5)
            cv2.putText(img, name, (x1+6,y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (0,200,255), 2)
            break

    cv2.imshow('Webcam', img)
    cv2.waitKey(1)
        
cv2.imshow('Webcam', img)
cv2.waitKey(1)