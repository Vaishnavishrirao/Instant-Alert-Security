import smtplib
from smtplib import SMTPException

sender = " "
receiver = [" "]
message = "Hello!"

try:
    session = smtplib.SMTP('smtp.gmail.com',587)
    session.ehlo()
    session.starttls()

    session.login(sender,' ')
    session.sendmail(sender,receiver,message)
    print("ok")
except SMTPException:
    print("error")
session.quit()

