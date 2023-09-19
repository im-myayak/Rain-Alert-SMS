import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
load_dotenv()


API_KEY = os.environ.get('API_KEY')
API_KEY_1 = "fe4d763501286137af72176476c942b1"
API_END_POINT = os.environ.get('API_END_POINT')
ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
LATITUDE = 58.159912
LONGITUDE = 8.018206
parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    'exclude': 'current,minutely,daily',
    "appid": API_KEY,
}
print(API_KEY,API_END_POINT)
response = requests.get(API_END_POINT, params=parameters)
response.raise_for_status()
weather_hourly = response.json()['hourly'][:12]
isRainList = [(True if x['weather'][0]['id'] < 700 else False) for x in weather_hourly]

if True in isRainList:
    # # while using a third party
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'http': os.environ['http_proxy']}
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body="It is going to rain today, Remember to bring an umbrella.",
        from_='+12514187168',
        to='+916281646095'
    )
    print(message.status)
