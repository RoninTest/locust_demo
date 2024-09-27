# random_booking_id.py
import random
import logging

logging.basicConfig(level=logging.INFO)


def get_random_booking_id(user):
    logging.info("Getting random booking ID...")
    response = user.client.get("/booking")

    if response.status_code == 200:
        booking_list = response.json()
        if booking_list:
            random_booking_id = random.choice(booking_list)["bookingid"]
            logging.info("Successfully retrieved random booking ID: %s", random_booking_id)
            return random_booking_id
        else:
            logging.warning("No bookings found in the response.")
    else:
        logging.error("Failed to get booking list. Status code: %d", response.status_code)
