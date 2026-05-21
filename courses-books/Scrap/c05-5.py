from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

# bs.find_all(lambda tag: len(tag.attrs) == 2)

images = bs.find_all('img',
                    {'src':re.compile('..\/img\/gifts/img.*.jpg')})

for image in images:
    print(image['src'])
