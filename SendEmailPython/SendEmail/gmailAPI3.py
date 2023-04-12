import smtplib

# set up the SMTP server for Gmail
smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

# login to your Gmail account
smtp_server.login('celsosilvajunior90@gmail.com', 'faxbnspldnkhacqv')

# create your email message
sender_email = 'celsosilvajunior90@gmail.com'
receiver_email = 'kleber.storani@luizalabs.com'
subject = 'Ola Garoto'
body = 'Como foi seu natal?'

message = f'Subject: {subject}\n\n{body}'

# send the email message
smtp_server.sendmail(sender_email, receiver_email, message)

# close the connection to the SMTP server
smtp_server.close()

print('Email sent successfully.')