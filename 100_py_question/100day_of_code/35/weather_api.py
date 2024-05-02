import requests

API_KAY = "29765317c01d2dadcbfc4991ea7cefe0"
LAT = 46.472253
LON = 30.747551
ENDPOINT = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KAY}"

response = requests.get(ENDPOINT)

print(response.json())