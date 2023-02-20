import smtplib



def enviar_mensaje(results):
    from_email = 'sendmails2023@gmail.com'
    from_email_password = 'bflynbtmwmbufiev'
    to_email = 'sendmails2023@gmail.com'
    smtp_server = "smtp.gmail.com"
    port = 587

    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls()
    server.login(from_email, from_email_password)

    message = "La lista es:\n" + "\n".join(results)

    server.sendmail(from_email, to_email, message)
    server.quit()


    

