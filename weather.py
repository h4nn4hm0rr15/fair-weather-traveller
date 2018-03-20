import requests
endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "London,UK", "units":"metric", "appid":"deb4c4aa994cc5ca9d606bd89e0c87d2
"}
response = requests.get(endpoint, params=payload)
print response.url
print response.status_code
print response.headers["content-type"]
data = response.json()
print data
temperature = data["main"]["temp"]
name = data["name"]
weather = data["weather"][0]["main"]
print u"It's {}C in {}, and the sky is {}".format(temperature, name, weather)
