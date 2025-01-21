import cv2
import numpy as np
import os
import smtplib

from smtplib import SMTPException

import smtplib
import imghdr
from email.message import EmailMessage
import glob

import time

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')   #load trained model
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter, the number of persons you want to include
id = 3 # persons


names = ['','vaishnavi','','']  #key in names, start from the second place, leave first empty

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:

    ret, img =cam.read()

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        # Check if confidence is less them 100 ==> "0" is perfect match
        con = (round(100 - confidence))
        if (con > 40):
            id = names[id]
            confi = "  {0}%".format(con)


        if(con <= 40):
            id = "salesman"
            confi = "  {0}%".format(con)
            cv2.imwrite("C://Users//hi//Desktop//python project//da43//img/img1.png", img)
            Sender_Email = "enter sender mail id"
            Reciever_Email = "enter reciever mail id"
            # Password = input('Enter your email account password: ')

            newMessage = EmailMessage()
            newMessage['Subject'] = ""
            newMessage['From'] = Sender_Email
            newMessage['To'] = Reciever_Email
            newMessage.set_content('!')

            with open('C://Users//hi//Desktop//python project//da43//img/img1.png', 'rb') as f:
                image_data = f.read()
                image_type = imghdr.what(f.name)
                image_name = f.name

            newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(Sender_Email, 'enter password')
                smtp.send_message(newMessage)

            removing_files = glob.glob('C://Users//hi//Desktop//python project//da43//img/img1.png')
            for i in removing_files:
                os.remove(i)

        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confi), (x+5,y+h-5), font, 1, (255,255,0), 1)

    cv2.imshow('camera',img)

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("\n end.......")
cam.release()
cv2.destroyAllWindows()
