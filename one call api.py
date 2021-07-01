from twilio.rest import Client
import requests

account_sid = "ACf1ba52d3ac06694341734af3126b2fc0"
auth_token = "e7720cc45deb217015c8e045a15d3dd6"
API_KEY = "1a6dc93f2a925fd1fb3107972fea8126"
parameters = {
    "lat": 26.452475,
    "lon": 87.271782,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
hourly_data = data["hourly"][:12]
will_rain = False
for id in hourly_data:
    weather_id = id["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain carry your umbrella☔",
        from_='+12182768905',
        to='Enter your phone number here'
    )
    print(message.status)
