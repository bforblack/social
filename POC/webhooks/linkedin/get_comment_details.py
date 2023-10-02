import requests

# Replace 'YOUR_ACCESS_TOKEN', 'URN_VALUE', and 'COMMENT_ID' with actual values
access_token = 'YOUR_ACCESS_TOKEN'
urn_value = 'shareUrn_or_ugcPostUrn_or_commentUrn'
comment_id = 'COMMENT_ID'

url = f"https://api.linkedin.com/v2/socialActions/{urn_value}/comments/{comment_id}"

headers = {
    "Authorization": f"Bearer {access_token}"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    comment_data = response.json()
    print("Comment data:", comment_data)
else:
    print("Error:", response.status_code)
    print("Response content:", response.text)
