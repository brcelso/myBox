import base64
from apiclient import errors
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from httplib2 import Http
from email.mime.text import MIMEText

def service_account_login():
	credentials = Credentials.from_service_account_file(
		'C:\Users\celso\OneDrive\Documentos\GitHub\myBox\winged-idiom-358615-cf17f1e89c57.json', 
		scopes=['https://www.googleapis.com/auth/gmail.send']
	)
	delegated_credentials = credentials.with_subject('me')
	gmail = build('gmail', 'v1', credentials=delegated_credentials)
	return gmail

def create(from_, subject, text):
	"""Create a message for an email

	Parameters
	----------
	from_ : [type]
		Email address of the sender
	subject : [type]
		 The subject of the email message
	text : [type]
		The text of the email message

	Returns
	-------
	[type]
		An object containing a base64url encoded email object
	"""

	message = MIMEText(text)
	message['from'] = from_
	message['to'] = "someone@<gsuite domain>".com
	message['subject'] = subject

	return {
		'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()
	}

def send(from_, subject, text):
	"""[summary]

	Parameters
	----------
	service : [type]
		Authorized Gmail API service instance
	message : [type]
		Message to be sent

	Returns
	-------
	[type]
		Sent Message
	"""

	try:
		message_ = create(from_=from_, subject=subject, text=text)
		service = service_account_login()
		message = (
			service.users()
			.messages()
			.send(userId='', body=message_)
			.execute()
		)
		print(f"Message Id: {message['id']}")

		return message

	except errors.HttpError as error:
		print(f'An error occurred: {error}')