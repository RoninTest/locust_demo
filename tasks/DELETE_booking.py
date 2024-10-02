# delete_booking.py
import logging

from util.base import BaseUser
from util.auth import authenticate
from util.random_booking_id import get_random_booking_id


def delete_booking(user):
    booking_id = get_random_booking_id(user)

    if not booking_id:
        print("No valid booking ID found. Cannot proceed with delete")
        return None

    logging.info("Starting authentication process for user: %s", user)
    token = authenticate(user)
    logging.info("Token successfully received: %s", token)

    if not token:
        print("Authentication failed. Cannot update booking.")
        return None

    response = user.client.delete(f"/booking/{booking_id}",
                                  headers={
                                      "Content-Type": "application/json",
                                      "Accept": "application/json",
                                      "Cookie": f"token={token}"
                                  })

    if response.status_code == 201:
        logging.info("Booking delete successfully. Booking ID: %s", booking_id)
    else:
        logging.error("Failed to delete booking. Status Code: %d", response.status_code)
        return None


class DeleteBookingUser(BaseUser):
    tasks = [delete_booking]
