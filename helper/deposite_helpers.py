import random

# %70 : True %30 : False
deposit_paid = random.choices([True, False], weights=[70, 30], k=1)[0]
