import requests

url = 'https://graph.facebook.com/v17.0/105150415943869/photos'
access_token = 'EAAathGdn1gcBANeoaIFGfRku2ZBxnTuYIsBCCgQ3EiYguYC4ZB5fnr0SfRZADJqVwBFDXhXu3mUMbXGW4R6USPAE98eaQI47epZALPZCzdKX8ppgQAUzKLlR3redQLkAfN4KjIxp7mj1LtrzLoJdHiuussu9Ql5nQ92BTutum05aaNU1ctCF6IHdvFYTiKoMT9rxL8S4gz2zK59dVpZBE3kfXld8jqgZBwZD'

params = {
    'access_token': access_token
}

image_path = "/home/sumit/Desktop/postManagementService/DataNext/src/python/social/socialHubIntegrationService/multimedia/artbreeder-image.jpg"

files = {
    'source': ('artbreeder-image.jpg', open(image_path, 'rb'), 'image/jpeg')
}

response = requests.post(url, params=params, files=files)


# Handle the response
if response.status_code == 200:
    print('Photo uploaded successfully!')
    print('Post ID:', response.json().get('id'))
else:
    print('Error uploading photo. Status code:', response.status_code)
    print('Error message:', response.json().get('error').get('message'))
