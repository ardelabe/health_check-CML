import smtplib
import email.message
import os

def send_email(body_email, receiver):  
    msg = email.message.Message()
    msg['Subject'] = "ALERTA DO SCRIPT HEALTH_CHECK"
    msg['From'] = 'naoresponder@cml.pr.gov.br'
    msg['To'] = receiver
    password = ''
    with open(os.path.dirname(os.path.realpath(__file__)) +'/pswd.txt') as f:
        password = f.read()
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body_email)
    s = smtplib.SMTP('192.168.1.2: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('emails.py says: email sent')

