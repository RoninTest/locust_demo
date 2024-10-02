# body.py
from random import randint
from helper.name_helpers import first_name, last_name
from helper.random_date_helpers import checkin_date, checkout_date
from helper.deposite_helpers import deposit_paid

total_price = randint(50, 100)


def generate_booking_data():
    body = {
        "firstname": first_name,
        "lastname": last_name,
        "totalprice": total_price,
        "depositpaid": deposit_paid,
        "bookingdates": {
            "checkin": checkin_date,
            "checkout": checkout_date
        }
    }
    return body
