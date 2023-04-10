import base64
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials

# Replace with your email address and service account json file path
USER_EMAIL = 'celsosilvajunior90@gmail.com'
SERVICE_ACCOUNT_FILE = 'winged-idiom-358615-cf17f1e89c57.json'

# Authorize with GMail API using service account credentials /n
creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, ['https://www.googleapis.com/auth/gmail.modify'])

service = build('gmail', 'v1', credentials=creds)


# Search for email with specific subject and sender
results = service.users().messages().list(userId='me', q='subject:hello from celsosilvajunior90@gmail.com').execute()
messages = results.get('messages', [])

if messages:
    for message in messages:
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        thread_id = msg['threadId']
        payload = msg['payload']
        headers = payload['headers']

        # Get the email sender
        for header in headers:
            if header['name'] == 'From':
                sender = header['value']

        # Get the email message body
        body = base64.urlsafe_b64decode(payload['body']['data']).decode('utf-8')

        # Create and send a reply message
        reply = 'Thank you for reaching out. I received your message and will get back to you shortly.'
        message = service.users().messages().send(userId='me', body={'threadId': thread_id, 'text': reply}).execute()

        print(f'Replied to {sender}:\n{reply}')
else:
    print('No messages found with the given search criteria.')