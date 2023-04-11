import smtplib

smtp_server = 'smtp.gmail.com'
port = 587  # For SSL
sender_email = "celsosilvajunior90@gmail.com"  # Enter your address
receiver_email = "gillthebot@gmail.com"  # Enter receiver address
password = "faxbnspldnkhacqv"

message = """\
Subject: BotTest

This message is sent from Python."""

try:
    # Create a secure SSL connection to the Gmail SMTP server
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()

    # Login to Gmail with your Gmail account username and password
    server.login(sender_email, password)

    # Send the email message
    server.sendmail(sender_email, receiver_email, message)
    print('Email sent successfully')
except Exception as e:
    # Print any error messages to the console
    print(e)
finally:
    # Logout of Gmail
    server.quit()
