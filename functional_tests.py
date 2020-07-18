from selenium import webdriver

options = webdriver.FirefoxOptions()
options.add_argument('-private')
options.add_argument('-headless')
with webdriver.Firefox(options=options) as browser:
    browser.get('http://localhost:8000')
    assert 'Django' in browser.title
