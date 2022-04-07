import datetime
import requests
import random

# creates date format. eg. 20220404
def build_date():
  date = datetime.datetime.now() + datetime.timedelta(days=1)
  return date.strftime("%Y%m%d")

_last_hour_block = 9
_hours = ["08", "11", "14", "17", "20"]

#format => hour_block [6,7,8,9,10]
booking_url = "https://us-central1-eiloborg.cloudfunctions.net/s4aapp?f=prenota&token=U2FsdGVkX19F5pEV0DKiW5Xpc9%2FUUSSBtFqN1r7900Q%3D&v1={}&v2=ED1&v3=^SER12^"

# format => date, hour, booking_number
access_url = "https://us-central1-eiloborg.cloudfunctions.net/s4aapp?f=accedi&token=U2FsdGVkX19F5pEV0DKiW5Xpc9%2FUUSSBtFqN1r7900Q%3D&v1={}*SER12*{}00*PRENOTAZIONE%20POSTO*Edificio%20A%20SPAZIO%20STUDIO%201%20piano%20terra%20ala%20sx%20{}"

# booking rooms: from 08.00 to 17.00
for i in range(6, _last_hour_block + 1):
  print(f"Booking {booking_url.format(i)}")
  r = requests.get(booking_url.format(i))
  print(f"Result: {r.text}")

# accessing rooms
for i in range(0, _last_hour_block - 5):
  date = build_date()
  hour = _hours[i]
  booking_number = random.randint(0, 104)
  print(f"Accessing {access_url.format(date, hour, booking_number)}")
  r = requests.get(access_url.format(date, hour, booking_number))
  print(f"Response: {r.text}")