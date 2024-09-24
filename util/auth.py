from locust import HttpUser
import json


class UserAuth(HttpUser):

    def on_start(self):
        self.token = None  # Token sadece auth olan task için kullanılacak

    def authenticate(self):
        # Auth request to get token
        response = self.client.post(
            "/auth",  # Endpoint for authentication
            headers={"Content-Type": "application/json"},
            data=json.dumps({
                "username": "admin",  # Your username
                "password": "password123"  # Your password
            })
        )

        # If auth is successful, save the token
        if response.status_code == 200:
            auth_response = response.json()
            self.token = auth_response['token']
            print(f"Authenticated successfully. Token: {self.token}")
        else:
            print(f"Authentication failed! Status Code: {response.status_code}")
