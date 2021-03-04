import face_recognition
from cv2 import cv2
import time
import os
from datetime import datetime


now = datetime.now()
time = now.strftime("%H:%M:%S")
name = ' '

def VidRecognition():
    global name
    video_capture = cv2.VideoCapture(0)

    Jarne_image = face_recognition.load_image_file(r"Images\Jarne.jpg")
    Jarne_face_encodings = face_recognition.face_encodings(Jarne_image) [0]

    known_face_encodings = [
        Jarne_face_encodings
    ]

    known_face_names = [
        "Jarne"
        
    ]


    while True:
        ret, frame = video_capture.read()

        rgb_frame = frame[:,:,::-1]


        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame,face_locations)

        for(top,right,bottom,left),face_encoding in zip(face_locations,face_encodings):

            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            name = "Unidentified User"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]



            cv2.rectangle(frame,(left,bottom-35),(right,bottom),(0,0,255),cv2.FILLED)
            font =cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left+6,bottom-6), font, 1.0, (255,255,255), 1)

        cv2.imshow("video",frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        if name == "Jarne":

            print("Access granted on video recognition")
            video_capture.release()
            cv2.destroyAllWindows()
            
            #textfile = open(r"logs\login logs\known_logins.txt","a")
            #textfile.write((name, " logged in at:", time))
            

            #textfile = open(r"logs\login logs\known_logins.txt","r")
            #print(textfile())
            return name
            


            

    
    video_capture.release()
    cv2.destroyAllWindows()
    return name

