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
    smtp_server = "mail.kian.digital"
    sender_email = "devops-certificates@kian.digital"
    receiver_email = ["r.forouzan@kian.digital"]
    password = "H9KtiVI42xjcWoQCSQZD"

    message = f"Subject: {subject}\n\n{body}"
    context = ssl.create_default_context()

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


hn = ["pwa.kiandigital.com","landing.neshanid.com","neshanid.io","gitlab.kian.digital","kiangroup.com","bt.sivacrm.com","demo.sivacrm.io"]
lhn = len(hn)

for i in range (0,lhn):
    try:
        hostname = hn[i]
        exp = verify_ssl_certificate(hostname)
        exp_month = exp[:3]
        exp_day = exp[4:6]
        # if exp_day[0] == ' ':
        #     exp_day = exp_day.replace(' ','0')
            # print(exp_day)
        exp_year = exp[16:20]
        exp_time = exp[7:12]
#        ct = datetime.datetime.now()
        cd = datetime.datetime.today()
        exp_date = exp_month + ' ' + exp_day + ' ' + exp_year #+ ' ' + exp_time
        # print(exp_date)
        # format = '%b %d %Y %I:%M'
        format = '%b %d %Y'
        exp_dtf = datetime.datetime.strptime(exp_date, format)
        tr = exp_dtf - cd
        dr = tr.days
        if dr > 30 :
            subject = "SSL Certificate Status"
            body = f"ssl certificate expiration date for {hostname} is going to expire in {dr} days"
            send_email(subject, body)
        elif 30 > dr > 15 :
            subject = "SSL Certificate Warning"
            body = f"ssl certificate expiration date for {hostname} is going to expire in {dr} days"
            send_email(subject, body)
        elif 15 > dr > 10:
            subject = "SSL Certificate Warning"
            body = f"ssl certificate expiration date for {hostname} is going to expire in {dr} days"
            send_email(subject, body)
        elif dr < 10:
            subject = "SSL Certificate Error"
            body = f"ssl certificate expiration date for {hostname} is going to expire in {dr} days"
            send_email(subject, body)
    except Exception as e:
        e = str(e)
        subject = "SSL Certificate Error"
        body = f"SSL Certificate status : " + e
        send_email(subject, body)