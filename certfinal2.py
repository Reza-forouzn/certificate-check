import certifi
import ssl
import socket
from cryptography import x509
import smtplib
import datetime

def verify_ssl_certificate(hostname):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ss:
            data = ss.getpeercert()
            notafter_date = data["notAfter"]
            return(notafter_date)

def send_email(subject, body):
    port = 587
    smtp_server = "mail.mail"
    sender_email = "email@email"
    receiver_email = ["email@email"]
    password = "password"

    message = f"Subject: {subject}\n\n{body}"
    context = ssl.create_default_context()

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


hn = ["comma seprated usrls"]
lhn = len(hn)

for i in range (0,lhn):
    try:
        hostname = hn[i]
        exp = verify_ssl_certificate(hostname)
        exp_month = exp[:3]
        exp_day = exp[4:6]
        exp_year = exp[16:20]
        exp_time = exp[7:12]
        cd = datetime.datetime.today()
        exp_date = exp_month + ' ' + exp_day + ' ' + exp_year
        format = '%b %d %Y'
        exp_dtf = datetime.datetime.strptime(exp_date, format)
        tr = exp_dtf - cd
        dr = tr.days
        if dr > 30 :
            subject = f"SSL Certificate Status for {hostname}"
            body = f"ssl certificate expiration date for {hostname} is going to expire in {dr} days"
            send_email(subject, body)
        elif 30 > dr > 15 :
            subject = f"SSL Certificate Warning for {hostname}"
            body = f"ssl certificate expiration date for {hostname} is going to expire in {dr} days"
            send_email(subject, body)
        elif 15 > dr > 10:
            subject = f"SSL Certificate Warning for {hostname}"
            body = f"ssl certificate expiration date for {hostname} is going to expire in {dr} days"
            send_email(subject, body)
        elif dr < 10:
            subject = f"SSL Certificate Error for {hostname}"
            body = f"ssl certificate expiration date for {hostname} is going to expire in {dr} days"
            send_email(subject, body)
    except Exception as e:
        e = str(e)
        subject = "SSL Certificate Error"
        body = f"SSL Certificate status : " + e
        send_email(subject, body)