from urllib.request import urlopen
import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup

html = urlopen('https://pythonscraping.com/wp-content/uploads/2021/08/home1.jpg')
print(html)

# image = Image.open(BytesIO(html.read()))
# image.show()

page = requests.get('http://pythonscraping.com/pages/page1.html')
print(page.text)


soup = BeautifulSoup(page.text)

print(soup.html.body.h1)
print(soup.body.h1)
print(soup.html.h1)
print(soup.h1)