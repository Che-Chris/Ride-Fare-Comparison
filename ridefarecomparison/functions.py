import collections
import math

from uber_rides.session import Session as Uber_Session
from uber_rides.client import UberRidesClient
from lyft_rides.auth import ClientCredentialGrant
from lyft_rides.session import Session as Lyft_Session
from lyft_rides.client import LyftRidesClient
from lyft_rides.auth import AuthorizationCodeGrant
from config import *

def getUberPrices(start_latitude, start_longitude, end_latitude, end_longitude, seat_count):
    uber_session = Uber_Session(server_token=UBER_SERVER_TOKEN)
    uber_client = UberRidesClient(uber_session)

    response = uber_client.get_price_estimates(start_latitude=start_latitude, start_longitude=start_longitude, end_latitude=end_latitude, end_longitude=end_longitude, seat_count=seat_count)

    estimate = response.json.get('prices')

    results = []
    for entry in estimate:
        tempdict = collections.OrderedDict()
        tempdict['ride_type'] = entry['localized_display_name']
        tempdict['estimate'] = entry['estimate']
        minutes = entry['duration']/60
        seconds = entry['duration']%60
        tempdict['duration'] = str(math.trunc(minutes)) +' minutes '+str(math.trunc(seconds))+' seconds'
        results.append(tempdict)

    return results

def getLyftPrices(start_lat, start_lng, end_lat, end_lng):
    lyft_auth_flow = ClientCredentialGrant(client_id=LYFT_CLIENT_ID, client_secret=LYFT_CLIENT_SECRET, scopes='public')
    lyft_session = lyft_auth_flow.get_session()

    lyft_client = LyftRidesClient(lyft_session)
    response = lyft_client.get_cost_estimates(start_lat, start_lng, end_lat, end_lng)

    estimate = response.json.get('cost_estimates')

    results = []
    for entry in estimate:
        tempdict = collections.OrderedDict()
        tempdict['ride_type'] = entry['ride_type']
        tempdict['estimate'] = '$'+ str(math.trunc(entry['estimated_cost_cents_min']/100))
        minutes = entry['estimated_duration_seconds']/60
        seconds = entry['estimated_duration_seconds']%60
        tempdict['duration'] = str(math.trunc(minutes)) +' minutes '+str(math.trunc(seconds))+' seconds'
        results.append(tempdict)

    return results
    # lyft_auth_flow = AuthorizationCodeGrant(
    #     LYFT_CLIENT_ID,
    #     LYFT_CLIENT_SECRET,
    # )
    # lyft_auth_url = auth_flow.get_authorization_url()
