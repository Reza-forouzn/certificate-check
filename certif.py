import certifi
import ssl
import socket
from cryptography import x509
import smtplib
import datetime

# def verify_ssl_certificate(hostname):
#     context = ssl.create_default_context(cafile=certifi.where())
#     with socket.create_connection((hostname, 443)) as sock:
#         with context.wrap_socket(sock, server_hostname=hostname) as ssock:
#             ssock.do_handshake()
#             cert = ssock.getpeercert()
#             print("certificate is valid")

            
# verify_ssl_certificate("dorsatrader.ir")

# hostname = "pwa.kiandigital.com"
# hostname = "dorsatrader.ir"
def verify_ssl_certificate(hostname):
    context = ssl.create_default_context()
    # print (context)
    # print(socket)
    with socket.create_connection((hostname, 443)) as sock:
        # print (socket)
        # print (sock)
        # print (type(sock))
        with context.wrap_socket(sock, server_hostname=hostname) as ss:
            # print (ss)
            # print(type(ss))
            # print("SSL/TLS version:",ss.version())
            # print()
            data = ss.getpeercert()
            # print("Data:",data)
            # print()
            # print(type(data))
            # print(data)
            notafter_date = data["notAfter"]
            print (type(notafter_date))
            # print("Expiry date:",notafter_date)
            return(notafter_date)
            print()
            
def send_email(subject, body):
    port = 587
    smtp_server = "mail.kian.digital"
    sender_email = "devops-monitoring@kian.digital"
    receiver_email = ["r.forouzan@kian.digital"]
    password = "4St4GkqctQw9CnL2wa66"

    message = f"Subject: {subject}\n\n{body}"
    context = ssl.create_default_context()

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

hostname = "pwa.kiandigital.com"
exp = verify_ssl_certificate(hostname)
print (exp)
exp_month = exp[:3]
# print(exp_month)
exp_day = exp[4:6]
# exp_day = int(exp_day)
# print(exp_day)
# print(type(exp_day))
exp_year = exp[16:20]
# exp_year = int(exp_year)
# print(exp_year)
exp_time = exp[7:12]
# print(exp_time)
# verify_ssl_certificate("dorsatrader.ir")
subject = "SSL Certificate Status"
body = f"ssl certificate expiration date for {hostname} is {exp}"
send_email(subject, body)
# t = time.strftime("%H:%M:%S", time.localtime())
# print (datetime.datetime.now())
ct = datetime.datetime.now()
print(ct)
print(type(ct))
# print (ct)
# print(ct.strftime('%b'))
# print(ct.day)
# def days_between(d1, d2):
#     d1 = datetime.strptime(d1, "%Y-%m-%d")
#     d2 = datetime.strptime(d2, "%Y-%m-%d")
#     return abs((d2 - d1).days)

## exp_dtf = datetime.datetime.strptime(exp, '%m/%d/%y %H:%M:%S')
##print(exp_dtf)

# def convert(date_time): 
#     format = '%b %d %Y %I:%M%p'
#     datetime_str = datetime.datetime.strptime(date_time, format) 
  
#     return datetime_str 
exp_date = exp_month + ' ' + exp_day + ' ' + exp_year + ' ' + exp_time
print (exp_date)
format = '%b %d %Y %I:%M'
exp_dtf = datetime.datetime.strptime(exp_date, format)
# print(exp_dtf)
# print(type(exp_dtf))
tr = exp_dtf - ct
# print(tr.days)
dr = tr.days
body = f"ssl certificate expiration date for {hostname} is going to expire in {dr} days"
send_email(subject, body)