import requests

# Set the tracking number for your package
tracking_number = 'YOUR_TRACKING_NUMBER_HERE'

# Set the URL for the Correios API
url = f'https://api.postmon.com.br/v1/rastreio/ect/{tracking_number}'

# Send a request to the API to get the tracking information
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Get the tracking information from the response
    tracking_info = response.json()

    # Print the tracking events for the package
    for event in tracking_info['historico']:
        print(f'{event["data"]} - {event["hora"]} - {event["local"]} - {event["mensagem"]}')
else:
    print('Failed to retrieve tracking information.')
