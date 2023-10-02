import json
import requests


def post_info(access_token, post_id):
    import requests

    url = f"https://graph.facebook.com/v17.0/{post_id}/comments?access_token={access_token}"

    response = requests.request("GET", url)

    # print(response.text)
    return response.json()
def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data. Status code: {response.status_code}")
        return None


def get_next_page_data(data):
    if 'paging' in data and 'next' in data['paging']:
        return fetch_data(data['paging']['next'])
    else:
        return None


def extract_comments(data):
    messages = []
    timestamps = []
    for item in data['data']:
        timestamps.append(item['created_time'])
        messages.append(item['message'])
    return timestamps, messages


def extract_all_comments(data):
    all_messages = []
    all_timestamps = []
    while data is not None:
        timestamps, messages = extract_comments(data)
        all_messages.extend(messages)
        all_timestamps.extend(timestamps)
        data = get_next_page_data(data)
    return all_timestamps, all_messages