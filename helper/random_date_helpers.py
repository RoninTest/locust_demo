from datetime import datetime, timedelta

current_date = datetime.now()

checkin_date = current_date.strftime("%Y-%m-%d")
checkout_date = (current_date + timedelta(days=3)).strftime("%Y-%m-%d")
