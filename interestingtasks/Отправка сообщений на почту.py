import smtplib
from email.mime.text import MIMEText
from email.header import Header

gmail_user = 'daniyar.kanu@gmail.com'
gmail_password = 'flyciti123'

sent_from = gmail_user
to = input('Почты: ')
to = to.split(' ')
#subject = ('Очень важно сообщение!'.encode('utf-8'), charset='utf-8')
body = 'Test 2022 Hello!'

email_text = """
From: %s
To: %s
Subject: %s
%s
""" % (sent_from, ", ".join(to), subject, body)
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_user, gmail_password)
server.sendmail(sent_from, to, email_text)
server.close()
print('Сообщение отправлено!')
