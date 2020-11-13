import smtplib

to=input("Enter the email of recipient:\n")
content=input("Enter content of mail:\n")

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('rashadahmed.work@gmail.com','Qwerty@12345')
    server.sendmail('rashadahmed.work@gmail.com',to,content)
    server.close

sendEmail(to,content)