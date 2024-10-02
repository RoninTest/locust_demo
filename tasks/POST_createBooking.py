from locust import tag
from util.base import BaseUser
from util.body import generate_booking_data


@tag('createBooking')
def create_booking(user):
    booking_data = generate_booking_data()

    response = user.client.post(
        "/booking",
        json=booking_data,
        headers={"Content-Type": "application/json"}
    )

    if response.status_code == 200 or response.status_code == 201:
        print("Booking created successfully:", response.json())
    else:
        print(f"Failed to create booking, status code: {response.status_code}")


class CreateBookingUser(BaseUser):
    tasks = [create_booking]
