import requests
api_key = "043e49cebb2f593627564f83cacb59a2"

base_url="https://api.openweathermap.org/data/2.5/weather"
city = (input("Enter city: "))
params = {"q":city, "appid":api_key, "units":"metric"}
response = requests.get(base_url, params = params)
if response.status_code==200:
    data = response.json
    temperature = data['main']['temp']
    print(temperature)