import requests
import os

file_path = "/home/sumit/Desktop/postManagementService/DataNext/src/python/social/socialHubIntegrationService/multimedia/image.jpg"


def upload_file_to_facebook(api_version, app_id, file_length, file_type, access_token):
    url = f"https://graph.facebook.com/{api_version}/{app_id}/uploads"
    params = {
        "file_length": file_length,
        "file_type": file_type,
        "access_token": access_token
    }

    response = requests.post(url, params=params)

    return response.json() if response.ok else None


if __name__ == "__main__":

    _api_version = "v17.0"
    _app_id = "1879634042410503"
    _file_length = os.stat(file_path).st_size
    _file_type = "image/jpg"
    _access_token = "EAAathGdn1gcBAOYwyDGQyuFWqZCpfayZCm2lU00127pJ8YEPGc8tfQS8rQ9LmSAy97uUK0eGAwDDdqznH5gQDuD851zZAhrx4e7kegctTRHjMrfQC5HT6A6j9IHHe9M622svHUX7qs0DhCZBfDmZARX4TKE71wl8HW9gUsLGW5aOHO7jTHHcW"

    result = upload_file_to_facebook(_api_version, _app_id, _file_length, _file_type, _access_token)

    if result:
        print("File uploaded successfully!")
        print("Response data:", result)
    else:
        print("Failed to upload the file.")
