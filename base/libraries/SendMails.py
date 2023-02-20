import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from decouple import config



def enviar_mensaje(results,user_env,passwor_env,recive_env):
    host = 'smtp.gmail.com'
    port = 587
    user = user_env
    password = passwor_env

    msg = MIMEMultipart()
    msg['From'] = user_env
    msg['To'] = recive_env
    msg['Subject'] = 'Links de mercado libre'

    body = ''
    num = 1
    for link in results:
        body += f'{num}. <a href="{link}">{link}</a><br>'
        num += 1
    msg.attach(MIMEText(body, 'html'))

    with smtplib.SMTP(host, port) as server:
        server.starttls()
        server.login(user, password)
        server.sendmail(user, msg['To'], msg.as_string())

