from locust import tag
from util.base import BaseUser


@tag('getBookingIds')
def get_booking_ids(user):
    user.client.get("/booking")


class GetBookingIds(BaseUser):
    tasks = [get_booking_ids]
