f=open("/mnt/accuracy.txt","r")
y=[]
file=f.readlines()
for line in file:
    y.append(float(line.strip()))
accuracy=str(y[0])
f.close()
print("Your model accurcacy is :",accuracy)
import smtplib, ssl
port = 465 #For SSL
smtp_server ="smtp.gmail.com"
sender_email="my@gmail.com"    #Sender's Mail Address
receiver_email="toyou@gmail.com"      #Receiver's Mail Address
password="**********"
if accuracy > "92":
    message="""    Subject: Report | Prediction Program
    
    CONGRATULATIONS! 
    Your code achieved {}% accuracy.""".format(accuracy)
else:
    message="""    Subject: Report | Prediction Program
    
    Train Again!
    Your code got {}% accuracy.""".format(accuracy)
    
context=ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email,password)
    server.sendmail(sender_email, receiver_email, message)
