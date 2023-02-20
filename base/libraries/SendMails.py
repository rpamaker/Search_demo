import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def enviar_mails(results,send_mails,gmail_password,gmail_account):
    host = 'smtp.gmail.com'
    port = 587
    user = send_mails
    password = gmail_password

    msg = MIMEMultipart()
    msg['From'] = send_mails
    msg['To'] = gmail_account
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

