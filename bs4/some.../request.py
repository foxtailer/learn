import requests

response = requests.get("https://www.google.com/")

#print(response.status_code)
#print(response.headers)
#print(response.content)  # Bite string
#print(response.text)


#*********************#
response2 = requests.get("https://www.google.com/" + "search?q=dog")
#print(response2.text)

params = {"q": "dog",
          "appid": APIKEY,
          "units": "metric"}
response2 = requests.get("https://www.google.com/", params=params)


if response  #==  if response.status_code == 200


#_-------------------------

headers = {"Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,ru;q=0.8",
    "Dnt": "1",
    "Host": "httpbin.org",
    "Referer": "https://httpbin.org/",
    "Sec-Ch-Ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-66aa5a51-7ce4539e1aa07e4e25f04583"
}
response2 = requests.get("https://httpbin.org/headers", headers=headers) # Return our haders back to as in response.text
# response2.text == headers


# For post request
data = {
  'param1': "value1"
}
response2 = requests.get("https://httpbin.org/headers", headers=headers, data=data)


#....
var = requests.Session()
var.get('site')


#####
if response.headers['Content-Type'] == "application/json":
  response.json()