from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


try:
    html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    print('It Worked!')
    soup = BeautifulSoup(html)
    # if (header := soup.h1) is not None:
    #     print(header)
    namelist = soup.find_all('span', {'class': 'green'})
    for name in set(namelist):
        print(name.get_text())

    '''
    find_all(['hl', 'h2', 'hЗ', 'h4', 'h5', 'hб'))
    find_all( 'span', {'class': [ 'green', 'red' ]})

    bs.find(id='text', _class='main')  # ==
    bs.find(attrs={'id': 'text', 'class': 'main})
    '''
finally:
    print('Done')