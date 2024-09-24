from locust import between

from tasks.createBooking import CreateBookingUser
from tasks.getBookingId import GetBookingId
from tasks.getBookingIds import GetBookingIds
from tasks.updateBooking import UpdateBookingUser


class MyUser:
    wait_time = between(1, 40)
    tasks = [  # GetBookingIds,
        # GetBookingId,
        # CreateBookingUser,
        UpdateBookingUser]
