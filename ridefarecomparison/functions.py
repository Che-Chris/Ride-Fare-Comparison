import collections

from uber_rides.session import Session
from uber_rides.client import UberRidesClient
from lyft_rides.auth import ClientCredentialGrant
from lyft_rides.session import Session
from lyft_rides.client import LyftRidesClient
from lyft_rides.auth import AuthorizationCodeGrant
from config import *

def getUberPrice(start_latitude, start_longitude, end_latitude, end_longitude, seat_count):
    uber_session = Session(server_token=UBER_SERVER_TOKEN)
    uber_client = UberRidesClient(uber_session)

    response = uber_client.get_price_estimates(start_latitude=start_latitude, start_longitude=start_longitude, end_latitude=end_latitude, end_longitude=end_longitude, seat_count=seat_count)

    estimate = response.json.get('prices')

    results = []
    for entry in estimate:
        tempdict = collections.OrderedDict()
        tempdict['display_name'] = entry['localized_display_name']
        tempdict['estimate'] = entry['estimate']
        tempdict['duration'] = entry['duration']
        results.append(tempdict)

    return results

def getLyftPrices():
    lyft_auth_flow = ClientCredentialGrant(client_id=YOUR_CLIENT_ID, client_secret=YOUR_CLIENT_SECRET, scopes=YOUR_PERMISSION_SCOPES)
    lyft_session = lyft_auth_flow.get_session()

    lyft_client = LyftRidesClient(session)
    response = client.get_cost(37.7833, -122.4167)
    cost = response.json.get('cost_estimates')

    # lyft_auth_flow = AuthorizationCodeGrant(
    #     LYFT_CLIENT_ID,
    #     LYFT_CLIENT_SECRET,
    # )
    # lyft_auth_url = auth_flow.get_authorization_url()
