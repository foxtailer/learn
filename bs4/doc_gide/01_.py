from bs4 import BeautifulSoup


html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<li><a href="/uk/cases/UKSC/2014/4.html">Brownlee for Judicial Review (Northern Ireland) </a><a title="Link to BAILII version" href="/uk/cases/UKSC/2014/4.html">[2014] UKSC 4</a> (29 January 2014)</li>

<p class="story">...</p>
"""


soup = BeautifulSoup(html_doc, 'html.parser')
# BeautifulSoup(markup, "lxml")
# BeautifulSoup(markup, "lxml-xml") / BeautifulSoup(markup, "xml")  // for speed
# BeautifulSoup(markup, "html5lib")  // render tree same as browser. Slow
''''Ways of open document'''
# with open("index.html") as fp:
#     soup = BeautifulSoup(fp, 'html.parser')
''''''
# soup = BeautifulSoup(response.text, 'lxml')  # requesst from requests.get(url, headers=headers)
''''''
# len(soup.contents)
# # 1
# soup.contents[0].name
# # 'html'
print(soup.prettify())
# <html>
#  <head>
#   <title>
#    The Dormouse's story
#   </title>
#  </head>
#  <body>
#   <p class="title">
#    <b>
#     The Dormouse's story
#    </b>
#...

soup.title  # Find first title tag in document
# <title>The Dormouse's story</title>
# type(soup.title)
# <class 'bs4.element.Tag'>
# same as: soup.find("head")
# <head><title>The Dormouse's story</title></head>

soup.title.name
# u'title'

soup.title.string
# u'The Dormouse's story'
# type(soup.title.string)
# # <class 'bs4.element.NavigableString'>

soup.title.parent.name
# u'head'

soup.p
# <p class="title"><b>The Dormouse's story</b></p>

soup.p['class']  # You can access a tag's attributes by treating the tag like a dictionary
# u'title'
'''
tag.attrs
# {'id': 'boldest'}
tag.attrs.keys()
# dict_keys(['id'])
'''

soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find(id="link3")
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

for link in soup.find_all('a'):
    print(link.get('href'))
# http://example.com/elsie
# http://example.com/lacie
# http://example.com/tillie

print(soup.get_text())
# The Dormouse's story
#
# The Dormouse's story
#
# Once upon a time there were three little sisters; and their names were
# Elsie,
# Lacie and
# Tillie;
# and they lived at the bottom of a well.
#
# ...

'''Content'''
head_tag = soup.head
head_tag
# <head><title>The Dormouse's story</title></head>

head_tag.contents
# [<title>The Dormouse's story</title>]

title_tag = head_tag.contents[0]
title_tag
# <title>The Dormouse's story</title>
title_tag.contents
# ['The Dormouse's story']

# The .descendants attribute lets you iterate over all of a tag's children, recursively
for child in head_tag.descendants:
    print(child)
# <title>The Dormouse's story</title>
# The Dormouse's story

# If there's more than one thing inside a tag, you can still look at just the strings. Use the .strings generator to see all descendant strings:
for string in soup.strings:
    print(repr(string))
    '\n'
# "The Dormouse's story"
# '\n'
# '\n'
# "The Dormouse's story"
# '\n'
# 'Once upon a time there were three little sisters; and their names were\n'
# 'Elsie'
# ',\n'
# 'Lacie'
# ...
for string in soup.stripped_strings:
    print(repr(string))
# "The Dormouse's story"
# "The Dormouse's story"
#...

print(''.join(soup.li.stripped_strings))