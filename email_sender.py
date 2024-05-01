import smtplib
import ssl
import json
from email.message import EmailMessage

f = open('creds.json')
data = json.load(f)

def send_email(message_list):
    email_sender = data['email']
    email_password = data['pass']
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        for i in range(len(message_list)):
            email_receiver = message_list[i][0]

            subject = 'NSU Advising Reminder'
            body = ''
            for j in range(1, len(message_list[i])):
                for k in range(len(message_list[i][j])):
                    body += ' '.join([str(elem)
                                      for elem in message_list[i][j][k]])
                    body += '\n'

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(body)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
