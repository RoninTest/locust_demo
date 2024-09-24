from random import randint

from locust import tag
from tasks.base import BaseUser
from datetime import datetime, timedelta


@tag('createBooking')
def create_booking(user):
    current_date = datetime.now()

    checkin_date = current_date.strftime("%Y-%m-%d")  # Sistem tarihi (string formatında)
    checkout_date = (current_date + timedelta(days=3)).strftime("%Y-%m-%d")
    # Gönderilecek veriler
    booking_data = {
        "firstname": "Roni",
        "lastname": "Rola",
        "totalprice": randint(50, 100),
        "depositpaid": True,
        "bookingdates": {
            "checkin": checkin_date,
            "checkout": checkout_date
        },
        "additionalneeds": "Park"
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
