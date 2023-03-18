# Learn to parse with BeautifulSoup 4

import bs4

with open(r'C:\Users\User\Desktop\glovo\git\learn\bs4\website.html', "r") as file:
    html = file.read()

soup = bs4.BeautifulSoup(html, 'html.parser')

print(soup.text)
