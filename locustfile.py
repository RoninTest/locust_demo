# locustfile.py
from locust import between

from tasks.DELETE_booking import DeleteBookingUser
from tasks.POST_createBooking import CreateBookingUser
from tasks.PUT_updateBooking import UpdateBookingUser


class MyUser:
    wait_time = between(1, 40)
    tasks = [CreateBookingUser,UpdateBookingUser, DeleteBookingUser]
