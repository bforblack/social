import requests

# Replace these with your actual values
developer_application_id = "211439663"
member_id = "zLqTygBP8S"
organization_id = "96072893"
access_token = "AQX_qX5ti8iEIo5tuuNa2jarpRtxcnylBDR9ylI6oT2sdxLju-lTK8w0RUSFMuo31qIRF_DJ56J9YcA-DPDL1SAX-FYiDiMzgwwoDwJDimoxwHbQKpPrvd0ZdlF7v05Vv0JEG_wg3RaNR2Xt5QlU86GYx9a_-ZolTgA5Env_wkN4wcoUuhPOpxsBNSec5y8cHD9zw7i1RHIm3Tc8bcQN_IxOrX4mLLsgSLrDYrI_dJoWfVv6oBx6JGYCjj_4_AyAyC5o89PHjK7lye5stK9DCgAZ7i2lVeW6PnCmvuR0RAv0Is9-2Q7ZJYBdk09QRPYDJpoczGckdGCfWgqJyUGHvg2Uqmlz4Q"
webhook_url = "https://9b3b-14-194-23-18.ngrok.io/linkedin"


url = (
    f"https://api.linkedin.com/rest/eventSubscriptions/"
    f"(developerApplication:urn%3Ali%3AdeveloperApplication%3A{developer_application_id},"
    f"user:urn%3Ali%3Aperson%3A{member_id},entity:urn%3Ali%3Aorganization%3A{organization_id},"
    f"eventType:ORGANIZATION_SOCIAL_ACTION_NOTIFICATIONS)"
)

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
    "X-Restli-Protocol-Version": "2.0.0",
    "LinkedIn-Version": '202306',
}

data = {
    "webhook": webhook_url
}

response = requests.put(url, json=data, headers=headers)

if response.status_code == 204:
    print("Subscription updated successfully")
else:
    print("Failed to update subscription:", response.status_code, response.text)
