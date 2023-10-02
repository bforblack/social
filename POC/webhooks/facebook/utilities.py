import requests


def get_facebook_conversations(page_id, access_token):

    url = f"https://graph.facebook.com/v17.0/{page_id}/conversations"

    params = {
        "fields": "participants",
        "access_token": access_token
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data

    else:
        error = f"Request to fetch facebook conversations failed with status code: {response.status_code} \n Error: {response.text}"
        return {"error": error}


def get_conversation_id(receiver, sender, page_id, access_token):

    conversations = get_facebook_conversations(page_id, access_token)

    print(conversations)

    conversation_id = None

    if not conversations.get('error'):
        conversations = conversations.get('data')

        flag = False

        while not flag:
            for conversation in conversations:
                participants = conversation.get('participants')

                _sender_ = participants.get('data')[0]
                sender_psid = _sender_.get('id')

                _receiver_ = participants.get('data')[-1]
                receiver_psid = _receiver_.get('id')

                if sender_psid == sender and receiver_psid == receiver:
                    conversation_id = conversation.get('id')
                    flag = True

    else:
        print(f"Could not fetch details for conversation between sender_psid: {sender} and receiver_psid: {receiver}")

    return conversation_id


def generate_message(text):
    message = "Thanks for your response. We will contact you shortly!"
    return message


def send_facebook_message(page_id, recipient_id, message_text, access_token):

    url = f"https://graph.facebook.com/v17.0/{page_id}/messages"

    params = {
        "recipient": f"{{\"id\":\"{recipient_id}\"}}",
        "message": f"{{\"text\":\"{message_text}\"}}",
        "messaging_type": "RESPONSE",
        "access_token": access_token
    }

    response = requests.post(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        error = f"Request to send reply failed with status code: {response.status_code} \n Error: {response.text}"
        return {"error": error}


def handle_text_message_event(text, sender, receiver, page_id, access_token):

    conversation_id = get_conversation_id(receiver, sender, page_id, access_token)

    if conversation_id:

        message = generate_message(text)

        messaged = send_facebook_message(page_id, sender, message, access_token)

        if not messaged.get('error'):
            print("Response to the message sent successfully!")
            print(messaged)

        else:
            print("Responding to the message failed!")
            print(messaged.get('error'))

        return False

    else:
        print("Could not fetch the details of this conversation!")
        return True


if __name__ == '__main__':

    _receiver = "103658366092003"
    _sender = "6214143868684717"
    _page_id = "103658366092003"
    _access_token = "EAAathGdn1gcBOybKTyoOrvLjCM1T8mrz6FTRlSVC2vtcDulXtZAeah4zkCLZBKgHES8LwuwWrwdBMqnZCLK5pKoXp1gZBkMkcOK0cvwGB9cL6uRCCLXIZBNftnTNs0qNN8h1qvp0tPWbM9v7c9m133waMZCNkP1Dmjrc1eQUgdLdpbnuYm4HUfiu27RHsWsAZBlI7QpHxxUBBRF4CsGjjHmBZAz3IKm4RoYZD"
    _text = "Hi... How are you?"

    response = handle_text_message_event(_text, _sender, _receiver, _page_id, _access_token)




