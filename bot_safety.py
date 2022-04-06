import datetime
import requests

# creates date format. eg. 20220404
def build_date():
  # date = datetime.datetime.now() + datetime.timedelta(days=1)
  date = datetime.datetime.now() + datetime.timedelta()
  return date.strftime("%Y%m%d")

_last_hour_block = 5
_hours = ["08", "11", "14", "17", "20"]

#format => hour_block [1,2,3,4,5]
booking_url = "https://us-central1-eiloborg.cloudfunctions.net/s4aapp?f=prenota&token=U2FsdGVkX19bvfN1LAXXs6mhQg7HorCTiiUNOn7iTbE%3D&v1={}&v2=ED1&v3=^SER12^"

# format => date, hour
access_url = "https://us-central1-eiloborg.cloudfunctions.net/s4aapp?f=accedi&token=U2FsdGVkX19F5pEV0DKiW5Xpc9%2FUUSSBtFqN1r7900Q%3D&v1={}*SER12*{}00*PRENOTAZIONE%20POSTO*Edificio%20A%20SPAZIO%20STUDIO%201%20piano%20terra%20ala%20sx%20"

# booking rooms: from 08.00 to 17.00
for i in range(1, _last_hour_block):
  print(f"Booking {booking_url.format(i)}")
  r = requests.get(booking_url.format(i))
  print(f"Result: {r.text}")

# accessing rooms
for i in range(0, _last_hour_block - 1):
  date = build_date()
  hour = _hours[i]
  print(f"Accessing {access_url.format(date, hour)}")
  r = requests.get(access_url.format(date, hour))
  print(f"Response: {r.text}")