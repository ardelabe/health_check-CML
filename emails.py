import smtplib
import email.message

# body_email = """
#     <p>kaghfkjhdkjhfdskj</p>
#     <p>Parágrafo2</p>
#     """

def send_email(body_email, receiver):  
    # body_email = """
    # <p>Parágrafo1</p>
    # <p>Parágrafo2</p>
    # """

    msg = email.message.Message()
    msg['Subject'] = "ALERTA DO SCRIPT HEALTH_CHECK"
    msg['From'] = 'andersonabe.dev@gmail.com'
    msg['To'] = receiver
    password = ''   
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('email sent')
