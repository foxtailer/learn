from urllib.request import urlopen                                    
from bs4 import BeautifulSoup 


html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, "lxml")                               

# titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
namelist = bs.findAll('span', {'class': ['green', 'red']})            

for name in namelist:                                                 
    print(name.get_text())

