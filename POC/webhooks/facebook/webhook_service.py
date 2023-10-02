from facebook import utilities as ut

from fastapi import FastAPI, Request, HTTPException
from datetime import datetime

app = FastAPI()

# Replace this with your own verify token
USER_VERIFY_TOKEN = "webhookuserintegrationissuccessful"
PAGE_VERIFY_TOKEN = "webhookpageintegrationissuccessful"
PERMISSIONS_VERIFY_TOKEN = "webhookpermissionsintegrationwassuccessful"
MESSENGER_VERIFY_TOKEN = "webhookmessengerintegrationwassuccessful"


@app.get("/facebook_user")
async def verify_facebook_user_webhook(request: Request):
    # Get the query parameters
    hub_mode = request.query_params.get("hub.mode")
    hub_verify_token = request.query_params.get("hub.verify_token")
    hub_challenge = request.query_params.get("hub.challenge")

    # Print the values of query parameters
    print("hub.mode:", hub_mode)
    print("hub.verify_token:", hub_verify_token)
    print("hub.challenge:", hub_challenge)

    # Verify the hub_mode and hub_verify_token
    if hub_mode == "subscribe" and hub_verify_token == USER_VERIFY_TOKEN:
        # Respond with the hub_challenge to complete the verification process
        return int(hub_challenge)
    else:
        raise HTTPException(status_code=403, detail="Verification failed")


@app.post("/facebook_user")
async def handle_facebook_user_webhook(request: Request):

    body = await request.json()

    if body:
        print("Event received...")
    else:
        raise HTTPException(status_code=403, detail="Verification failed")


@app.get("/facebook_page")
async def verify_facebook_pages_webhook(request: Request):
    # Get the query parameters
    hub_mode = request.query_params.get("hub.mode")
    hub_verify_token = request.query_params.get("hub.verify_token")
    hub_challenge = request.query_params.get("hub.challenge")

    # Print the values of query parameters
    print("hub.mode:", hub_mode)
    print("hub.verify_token:", hub_verify_token)
    print("hub.challenge:", hub_challenge)

    # Verify the hub_mode and hub_verify_token
    if hub_mode == "subscribe" and hub_verify_token == PAGE_VERIFY_TOKEN:
        # Respond with the hub_challenge to complete the verification process
        return int(hub_challenge)
    else:
        raise HTTPException(status_code=403, detail="Verification failed")


@app.post("/facebook_page")
async def handle_facebook_pages_webhook(request: Request):
    body = await request.json()

    data = body.get('entry')[0].get('changes')[0]
    update = data.get('field')

    if update == 'mention':
        value = data.get('value')
        post_id = value.get('post_id')
        sender_name = value.get('sender_name')
        sender_id = value.get('sender_id')
        item = value.get('post')
        action = value.get('verb')
        print(post_id, sender_name, sender_id, item, action)

    elif update == 'feed':
        value = data.get('value')
        item = value.get('item')
        post_id = value.get('post_id')
        action = value.get('verb')
        created_time = value.get('created_time')
        message = value.get('message')
        from_name = value.get('from').get('name')
        from_id = value.get('from').get('id')
        print(item, post_id, action, created_time, message, from_name, from_id)

    else:
        raise HTTPException(status_code=403, detail="Verification failed")


@app.get("/facebook_permissions")
async def verify_facebook_permissions_webhook(request: Request):
    # Get the query parameters
    hub_mode = request.query_params.get("hub.mode")
    hub_verify_token = request.query_params.get("hub.verify_token")
    hub_challenge = request.query_params.get("hub.challenge")

    # Print the values of query parameters
    print("hub.mode:", hub_mode)
    print("hub.verify_token:", hub_verify_token)
    print("hub.challenge:", hub_challenge)

    # Verify the hub_mode and hub_verify_token
    if hub_mode == "subscribe" and hub_verify_token == PERMISSIONS_VERIFY_TOKEN:
        # Respond with the hub_challenge to complete the verification process
        return int(hub_challenge)
    else:
        raise HTTPException(status_code=403, detail="Verification failed")


@app.post("/facebook_permissions")
async def handle_facebook_permissions_webhook(request: Request):
    body = await request.json()
    print(body)
    print(datetime.now())
    if body:
        print("Event received...")
    else:
        raise HTTPException(status_code=403, detail="Verification failed")


@app.get("/facebook_messenger")
async def verify_facebook_messenger_webhook(request: Request):
    # Get the query parameters
    hub_mode = request.query_params.get("hub.mode")
    hub_verify_token = request.query_params.get("hub.verify_token")
    hub_challenge = request.query_params.get("hub.challenge")

    # Print the values of query parameters
    print("hub.mode:", hub_mode)
    print("hub.verify_token:", hub_verify_token)
    print("hub.challenge:", hub_challenge)

    # Verify the hub_mode and hub_verify_token
    if hub_mode == "subscribe" and hub_verify_token == MESSENGER_VERIFY_TOKEN:
        # Respond with the hub_challenge to complete the verification process
        return int(hub_challenge)
    else:
        raise HTTPException(status_code=403, detail="Verification failed")


@app.post("/facebook_messenger")
async def handle_facebook_messenger_webhook(request: Request):
    body = await request.json()

    try:
        print("......Event received......")
        print(f"Current Time: {datetime.now()}")

        receiver_type = body.get('object')
        data = body.get('entry')[0]

        event_received_time = data.get('time')
        messaging_data = data.get('messaging')[0]
        sender_id = messaging_data.get('sender').get('id')
        receiver_id = messaging_data.get('recipient').get('id')
        message_sent_time = messaging_data.get('timestamp')
        message_data = messaging_data.get('message')
        message_id = message_data.get('mid')

        print(f"Event Receiver Type: {receiver_type}")
        print(f"Event Received Time: {event_received_time}")
        print(f"Sender ID: {sender_id}")
        print(f"Receiver ID: {receiver_id}")
        print(f"Message Sent Time: {message_sent_time}")
        print(f"Message ID: {message_id}")

        if sender_id in ['103658366092003']:
            return True

        if message_data.get('text'):
            message_text = message_data.get('text')
            print(f"Message Text: {message_text}")

            if receiver_id == "103658366092003":
                access_token = "EAAathGdn1gcBOybKTyoOrvLjCM1T8mrz6FTRlSVC2vtcDulXtZAeah4zkCLZBKgHES8LwuwWrwdBMqnZCLK5pKoXp1gZBkMkcOK0cvwGB9cL6uRCCLXIZBNftnTNs0qNN8h1qvp0tPWbM9v7c9m133waMZCNkP1Dmjrc1eQUgdLdpbnuYm4HUfiu27RHsWsAZBlI7QpHxxUBBRF4CsGjjHmBZAz3IKm4RoYZD"

            response = ut.handle_text_message_event(message_text, sender_id, receiver_id, receiver_id, access_token)

            return response

        else:
            attachments = message_data.get('attachments')
            if attachments:
                for attachment in attachments:
                    attachment_type = attachment.get('type')
                    attachment_payload = attachment.get('payload')
                    attachment_url = attachment_payload.get('url')
                    print(f"Attachment Type: {attachment_type}")
                    print(f"Attachment URL: {attachment_url}")
        return True

    except Exception as e:
        raise HTTPException(status_code=403, detail=str(e))
