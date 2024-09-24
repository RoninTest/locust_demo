from locust import task, tag
from tasks.base import BaseUser


@tag('createBooking')
def create_booking(user):
    # Gönderilecek veriler
    booking_data = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    # POST isteğini gönderme
    response = user.client.post(
        "/booking",
        json=booking_data,  # Veriyi JSON olarak gönderiyoruz
        headers={"Content-Type": "application/json"}  # Doğru başlık ekleniyor
    )

    # Cevap başarılıysa
    if response.status_code == 200 or response.status_code == 201:
        print("Booking created successfully:", response.json())
    else:
        print(f"Failed to create booking, status code: {response.status_code}")


class CreateBookingUser(BaseUser):
    tasks = [create_booking]
