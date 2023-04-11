import smtplib
import time

# Set up SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("gillthebot@gmail.com", "xuigobopavjgqaql")

# Create message
msg = "Hello, this is a test email sent using Python!"

# Send email every 5 minutes
while True:
    server.sendmail("gillthebot", "celsosilvajunior90@gmail.com", msg)
    print("Email sent!")
    time.sleep(300)