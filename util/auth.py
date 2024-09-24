# auth.py
import json


def authenticate(user):
    """Authenticate and return token"""
    # Authentication request to get token
    response = user.client.post(
        "/auth",  # Auth endpoint
        headers={"Content-Type": "application/json"},
        data=json.dumps({
            "username": "admin",  # Kullanıcı adı
            "password": "password123"  # Şifre
        })
    )

    # Başarılı olursa, token'ı döner
    if response.status_code == 200:
        auth_response = response.json()
        token = auth_response.get("token")
        print(f"Authenticated successfully. Token: {token}")
        return token
    else:
        print(f"Authentication failed! Status Code: {response.status_code}")
        return None
