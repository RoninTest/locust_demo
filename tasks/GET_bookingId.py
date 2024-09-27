from locust import tag
from tasks.base import BaseUser
from util.random_booking_id import get_random_booking_id


@tag('getBookingId')
def get_booking_id(user):
    random_booking_id = get_random_booking_id(user)
    if random_booking_id:
        user.client.get(f"/booking/{random_booking_id}")
    else:
        print("No valid booking ID found.")


class GetBookingId(BaseUser):
    tasks = [get_booking_id]
