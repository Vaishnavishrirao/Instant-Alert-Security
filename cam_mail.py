import smtplib
import imghdr
from email.message import EmailMessage
import glob
import os
import cv2
import time


cam = cv2.VideoCapture(0)
res, image= cam.read()
if res:
    # showing result, it take frame name and image
    # output
    cv2.imshow("img", image)

    # saving image in local storage
    cv2.imwrite("C://Users//hi//Desktop//da43//img/img1.png", image)

    # If keyboard interrupt occurs, destroy image
    # window
    a=1
while True:
    if a==1:
        break

#cam.release()
    #cv2.destroyAllWindows()

Sender_Email = " "
Reciever_Email = " "
#Password = input('Enter your email account password: ')

newMessage = EmailMessage()
newMessage['Subject'] = "Check out the new logo"
newMessage['From'] = Sender_Email
newMessage['To'] = Reciever_Email
newMessage.set_content('Let me know what you think. Image attached!')

with open('C://Users//hi//Desktop//da43//img/img1.png', 'rb') as f:
    image_data = f.read()
    image_type = imghdr.what(f.name)
    image_name = f.name

newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(Sender_Email, ' ')
    smtp.send_message(newMessage)

removing_files = glob.glob('C://Users//hi//Desktop//da43//img/img1.png')
for i in removing_files:
    os.remove(i)

