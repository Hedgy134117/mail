import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

server.connect("smtp.gmail.com", 465)

server.ehlo()
print(server.ehlo())

server.login("user_email", "user_password")
print(server.login("user_email", "user_password"))

for i in range(10):
    server.sendmail("sender_email", "receiver_email",  "Subject: Title\nBody")
    print(server.sendmail("sender_email", "receiver_email",  "Subject: Title\nBody"))


print(server.quit())

