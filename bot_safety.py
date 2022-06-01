import datetime
import requests
import random
from threading import Thread

# creates date format. eg. 20220404
def build_date():
  date = datetime.datetime.now()
  # date = datetime.datetime.now() + datetime.timedelta(days=1)
  return date.strftime("%Y%m%d")

# _first_hour_block = 1
_first_hour_block = 6
# _last_hour_block = 5
_last_hour_block = 10
_hours = ["08", "11", "14", "17", "20"]

_headers = {
  "origin" : "https://gosafety.web.app",
  "referer" : "https://gosafety.web.app/"
}

# users token
tokens = [
  "U2FsdGVkX1/ULpYErMXNHUCWW3cKMb9LTtCpLTi4qnI=", # lorenzo
  "U2FsdGVkX1/AjbnWwHiEIymZH0ip9fExuO3HTxpMQgA=", # caio
  "U2FsdGVkX187wl55oRxdyAutn7SQAnJZOhnVK8ACp8M%3D" # jack
]

#format => hour_block [6,7,8,9,10]
booking_url = "https://us-central1-eiloborg.cloudfunctions.net/s4aapp2?f=prenota&token={}%3D&v1={}&v2=ED1&v3=Edificio%20A%20SPAZIO%20STUDIO%201%20piano%20terra%20ala%20sx^SER12^{}"

# format => date, hour, booking_number
access_url = "https://us-central1-eiloborg.cloudfunctions.net/s4aapp2?f=accedi&token={}%3D&v1={}*SER12*{}00*PRENOTAZIONE%20POSTO*Edificio%20A%20SPAZIO%20STUDIO%201%20piano%20terra%20ala%20sx%20%23{}"


def book_function(_first_hour_block, _last_hour_block):
  # booking rooms and accessing rooms for each user
  for token in tokens:
    # booking rooms: from 08.00 to 17.00
    for i in range(_first_hour_block, _last_hour_block + 1):
      booking_number = random.randint(0, 104)
      print(f"Booking {booking_url.format(token, i, booking_number)}")
      r = requests.get(booking_url.format(token, i, booking_number), headers=_headers)
      print(f"Result: {r.text}")

    # accessing rooms
    # for i in range(0, _last_hour_block):
    #   date = build_date()
    #   hour = _hours[i]
    #   booking_number = random.randint(0, 104)
    #   print(f"Accessing {access_url.format(token, date, hour, booking_number)}")
    #   r = requests.get(access_url.format(token, date, hour, booking_number), headers=_headers)
    #   print(f"Response: {r.text}")

t1 = Thread(target=book_function, args=(1,5))
t2 = Thread(target=book_function, args=(5,10))

t1.start()
t2.start()