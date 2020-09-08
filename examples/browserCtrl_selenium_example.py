from selenium import webdriver

# Using Selenium webdriver to open Firefix tab and navigate to URL
browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')

# Using CSS selector to locate HTML element (here: a specific link)
# and store it in a WebElement object
elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a:nth-child(1)')

# Click the link
elem.click()

# Using send_keys() and submit() to use a search field
# Note: there is no search field on the site
# searchElem = browser.find_element_by_css_selector('.search-field')
# searchElem.send_keys('zophie')
# searchElem.submit()

# Using various browser control commands
# browser.back()
# browser.forward()
# browser.refresh()
# browser.quit()


# Reference: https://selenium-python.raedthedocs.org
