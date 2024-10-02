# update_booking.py
import json

from tasks.base import BaseUser
from util.auth import authenticate
from util.random_booking_id import get_random_booking_id
from util.body import generate_booking_data
import logging

logging.basicConfig(level=logging.INFO)


def update_booking(user):
    booking_id = get_random_booking_id(user)

    if not booking_id:
        print("No valid booking ID found. Cannot proceed with update.")
        return None

    logging.info("Starting authentication process for user: %s", user)
    token = authenticate(user)
    logging.info("Token successfully received: %s", token)

    if not token:
        print("Authentication failed. Cannot update booking.")
        return None

    update_data = generate_booking_data()

    response = user.client.put(f"/booking/{booking_id}",
                               headers={
                                   "Content-Type": "application/json",
                                   "Accept": "application/json",
                                   "Cookie": f"token={token}"
                               },
                               data=json.dumps(update_data)
                               )

    if response.status_code == 200:
        logging.info("Booking updated successfully. Booking ID: %s", booking_id)
    else:
        logging.error("Failed to update booking. Status Code: %d", response.status_code)
        return None


class UpdateBookingUser(BaseUser):
    tasks = [update_booking]
