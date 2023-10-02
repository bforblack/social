import hashlib
import hmac
import json

from facebook import utilities as ut
from fastapi import FastAPI, Request, HTTPException
from starlette.responses import JSONResponse

app = FastAPI()

APP_CLIENT_SECRET = "g9lFln33nPZUbUIb"


def calculate_hmac_sha256(secret: str, data: bytes) -> str:
    secret_bytes = bytes(secret, "utf-8")
    return hmac.new(
        secret_bytes,
        data,
        hashlib.sha256
    ).hexdigest()


@app.get("/linkedin")
async def verify_facebook_user_webhook(request: Request):

    challenge_code = request.query_params.get('challengeCode')
    application_id = request.query_params.get('applicationId')

    if application_id and challenge_code:
        client_secret = APP_CLIENT_SECRET

        signature = hmac.new(
            bytes(client_secret, "utf-8"),
            bytes(challenge_code, "utf-8"),
            hashlib.sha256
        ).hexdigest()

        # Prepare the JSON response
        response_data = {
            "challengeCode": challenge_code,
            "challengeResponse": signature
        }

        return JSONResponse(content=response_data, headers={"content-type": "application/json"})

    raise HTTPException(status_code=403, detail="Verification failed")


@app.post("/linkedin")
async def handle_facebook_user_webhook(request: Request):
    request_body_bytes = await request.body()

    request_body_string = request_body_bytes.decode("utf-8")
    print("Request Body Content: ")
    print(request_body_string)

    event = json.loads(request_body_string)

    prefixed_request_body = b"hmacsha256=" + request_body_bytes
    received_signature = request.headers.get('X-LI-Signature')
    calculated_signature = calculate_hmac_sha256(APP_CLIENT_SECRET, prefixed_request_body)

    if received_signature == calculated_signature:
        notifications = event.get('notifications')
        print(f"Number of Notifications: {len(notifications)}")
        return JSONResponse(content={"message": "Verification successful"})
    else:
        raise HTTPException(status_code=403, detail="Verification failed")
