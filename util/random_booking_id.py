# random_booking_id.py
import random


def get_random_booking_id(user):
    response = user.client.get("/booking")

    if response.status_code == 200:
        booking_list = response.json()
        if booking_list:
            return random.choice(booking_list)["bookingid"]
        else:
            print("Booking list is empty.")
            return None
    else:
        print(f"Failed to fetch booking list, status code: {response.status_code}")
        return None
