# auth.py
import json
import logging

logging.basicConfig(level=logging.INFO)


def authenticate(user):
    response = user.client.post(
        "/auth",
        headers={"Content-Type": "application/json"},
        data=json.dumps({
            "username": "admin",
            "password": "password123"
        })
    )

    if response.status_code == 200:
        auth_response = response.json()
        token = auth_response.get("token")
        logging.info("Authenticated successfully. Token: %s", token)
        return token
    else:
        logging.error("Authentication failed for user: %s. Status Code: %d", user, response.status_code)
        return None
