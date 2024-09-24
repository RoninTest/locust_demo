from locust import between

from tasks.getBookingId import GetBookingId
from tasks.getBookingIds import GetBookingIds


class MyUser:
    wait_time = between(1, 40)
    tasks = [GetBookingIds,
             GetBookingId]
