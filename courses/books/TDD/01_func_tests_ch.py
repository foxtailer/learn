'''
Terminology:
Functional Test == Acceptance Test == End-to-End Test
What I call functional tests, some people prefer to call acceptance tests, or end-to-end
tests. The main point is that these kinds of tests look at how the whole application
functions, from the outside. Another term is black box test, because the test doesn’t
know anything about the internals of the system under test.
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.binary_location = "/home/zoy/chrome-linux64/chrome"
driver = webdriver.Chrome(service=Service("/usr/local/bin/chromedriver"), options=chrome_options)
driver.get("http://localhost:8000")

assert "The install worked successfully" in driver.page_source

driver.quit()

