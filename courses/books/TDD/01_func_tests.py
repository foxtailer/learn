'''
Terminology:
Functional Test == Acceptance Test == End-to-End Test
What I call functional tests, some people prefer to call acceptance tests, or end-to-end
tests. The main point is that these kinds of tests look at how the whole application
functions, from the outside. Another term is black box test, because the test doesn’t
know anything about the internals of the system under test.
'''

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://localhost:8000')
assert 'Django' in browser.title
