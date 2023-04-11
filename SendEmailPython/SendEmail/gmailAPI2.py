import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Login details for SMTP server
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = 'celsosilvajunior90@gmail.com'
SMTP_PASSWORD = 'faxbnspldnkhacqv'

# Create SMTP connection
smtp_conn = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
smtp_conn.ehlo()
smtp_conn.starttls()
smtp_conn.login(SMTP_USERNAME, SMTP_PASSWORD)

# Message to be sent in reply
reply_msg = MIMEMultipart()
reply_msg['From'] = 'celsosilvajunior90@gmail.com'
reply_msg['To'] = 'celsosilvajunior90@gmail.com'
reply_msg['Subject'] = 'Re: teste'
reply_msg.attach(MIMEText('This is a reply to your original email message.'))

# Send the reply
smtp_conn.sendmail(SMTP_USERNAME, 'celsosilvajunior90@gmail.com', reply_msg.as_string())

# Close the SMTP connection
smtp_conn.quit()