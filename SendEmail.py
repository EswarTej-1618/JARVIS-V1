from email.message import EmailMessage
import smtplib
# from decouple import config


EMAIL = "##############@gmail.com"
PASSKEY = "**** **** **** ****" #use app key 

def send_email(receiver_add,subject,message):
    try:
        email = EmailMessage()
        email['To'] = receiver_add
        email['Subject'] = subject
        email['From'] = EMAIL
        
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSKEY)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    