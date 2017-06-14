from uber_rides.session import Session
from uber_rides.client import UberRidesClient
from config import *

session = Session(server_token=UBER_SERVER_TOKEN)
client = UberRidesClient(session)

def getUberPrice(start_latitude, start_longitude, end_latitude, end_longitude, seat_count):
    response = client.get_price_estimates(start_latitude=start_latitude, start_longitude=start_longitude, end_latitude=end_latitude, end_longitude=end_longitude, seat_count=seat_count)

    estimate = response.json.get('prices')

    return estimate
