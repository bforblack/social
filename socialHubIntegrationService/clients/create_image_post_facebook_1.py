import requests

page_id = "103658366092003"
path_to_photo = "https://cdn.pixabay.com/photo/2015/03/10/17/23/youtube-667451_960_720.png"
page_access_token = "EAAathGdn1gcBOZBoQCq8Cogy4YUBSjT7iKqZAyQW7nTxJUmVX2zgskd16ZCwsVyN3HQZCuKuYvog7SBRPJHMflgZCrkIJA4VXL2d7At7VTRuRVIFGqBzS7H3Cg5JsS1fveYZAhtDK41O0lQfphiGJqyy8hAO7kR1rI2sea3hAenLx3ZBzJZC9WD95DDR2JyiBXfxtOd7kqQZD"

url = f"https://graph.facebook.com/v17.0/{page_id}/photos"

headers = {
        "Authorization": f"Bearer {page_access_token}"
    }

data = {
    "message": "This is not awesome...",
    "url": path_to_photo,
}

response = requests.post(url, headers=headers, data=data)

print(response.status_code)
print(response.text)
