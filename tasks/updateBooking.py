# update_booking.py
import json
from datetime import datetime, timedelta
from random import randint

from tasks.base import BaseUser
from util.auth import authenticate  # auth.py'deki authenticate fonksiyonunu içe aktarıyoruz
from util.random_booking_id import get_random_booking_id  # random_booking_id.py'deki fonksiyonu içe aktarıyoruz


def update_booking(user):
    """Dinamik olarak bir booking id alır, auth yapar ve güncelleme işlemi yapar"""

    # 1. Dinamik olarak rastgele bir booking ID alıyoruz
    booking_id = get_random_booking_id(user)

    # Eğer booking_id alınamazsa işlemi durduruyoruz
    if not booking_id:
        print("No valid booking ID found. Cannot proceed with update.")
        return None

    # 2. İlk olarak authenticate ile token alıyoruz
    token = authenticate(user)

    # Eğer token alınmazsa işlemi durduruyoruz
    if not token:
        print("Authentication failed. Cannot update booking.")
        return None

    current_date = datetime.now()

    checkin_date = current_date.strftime("%Y-%m-%d")  # Sistem tarihi (string formatında)
    checkout_date = (current_date + timedelta(days=3)).strftime("%Y-%m-%d")

    # 3. Güncelleme için gönderilecek veri
    update_data = {
        "firstname": "Ronin",
        "lastname": "Roni",
        "totalprice": randint(50, 100),
        "depositpaid": True,
        "bookingdates": {
            "checkin": checkin_date,
            "checkout": checkout_date
        },
        "additionalneeds": "Breakfast"
    }

    # 4. PUT isteği ile güncelleme
    response = user.client.put(f"/booking/:{booking_id}",
                               headers={
                                   "Content-Type": "application/json",
                                   "Accept": "application/json",
                                   "Cookie": f"token={token}"  # Token'ı header olarak ekliyoruz
                               },
                               data=json.dumps(update_data)
                               )

    # Başarılı olursa sonucu yazdır
    if response.status_code == 200:
        print(f"Booking updated successfully. Booking ID: {booking_id}")
        return response.json()
    else:
        print(f"Failed to update booking. Status Code: {response.status_code}")
        return None


class UpdateBookingUser(BaseUser):
    tasks = [update_booking]
