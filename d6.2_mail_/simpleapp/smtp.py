import smtplib
from email.mime.text import MIMEText

msg = MIMEText('This is a test email.')
msg['Subject'] = 'Test'
msg['From'] = 'example@yandex.ru'
msg['To'] = 'recipient@example.com'

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login('example@yandex.ru', 'eabozqdfibvujmby')  # Пароль приложения
server.sendmail('example@yandex.ru', 'recipient@example.com', msg.as_string())
server.quit()
