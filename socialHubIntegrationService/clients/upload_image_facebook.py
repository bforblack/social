import requests


def upload_file_to_facebook(api_version, upload_session_id, access_token, file_name):
    url = f"https://graph.facebook.com/{api_version}/{upload_session_id}"
    headers = {
        "Authorization": f"OAuth {access_token}",
        "file_offset": "0"
    }

    with open(file_name, "rb") as file:
        data = file.read()

    response = requests.post(url, headers=headers, data=data)

    return response.json() if response.ok else None


_api_version = "v17.0"
_upload_session_id = "upload:MTphdHRhY2htZW50OjNkYjZjOWVlLWU5OTgtNDJlNS1iYzQxLWYzMDZjOGUwY2MxYj9maWxlX2xlbmd0aD00OTg4OSZmaWxlX3R5cGU9aW1hZ2UlMkZqcGc=?sig=ARY42qNaMvZUcZrdxDU"
_access_token = "EAAathGdn1gcBAOYwyDGQyuFWqZCpfayZCm2lU00127pJ8YEPGc8tfQS8rQ9LmSAy97uUK0eGAwDDdqznH5gQDuD851zZAhrx4e7kegctTRHjMrfQC5HT6A6j9IHHe9M622svHUX7qs0DhCZBfDmZARX4TKE71wl8HW9gUsLGW5aOHO7jTHHcW"
_file_name = "/home/sumit/Desktop/postManagementService/DataNext/src/python/social/socialHubIntegrationService/multimedia/image.jpg"

result = upload_file_to_facebook(_api_version, _upload_session_id, _access_token, _file_name)
if result:
    print("File uploaded successfully!")
    print("Response data:", result)
else:
    print("Failed to upload the file.")

# file_handle = "4::aW1hZ2UvanBn:ARYqk9kQuH5WZu6E2cT7JLFvxHnHSmc3rqKWZymzbOQU8Ww8vWlQO18-lzQtb3RtxiJtxKYIK0FRA3CAotjD4w_DW0pqRsPqj9H-4T1oKUJQ4g:e:1690618629:1879634042410503:100093371499451:ARZkyFeaFcodX6ybCmc"