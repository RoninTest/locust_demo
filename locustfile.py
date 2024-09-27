from locust import between


from tasks.PUT_updateBooking import UpdateBookingUser


class MyUser:
    wait_time = between(1, 40)
    tasks = [UpdateBookingUser]
