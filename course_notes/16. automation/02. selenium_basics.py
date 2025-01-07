# ==== selenium basics ====

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

service = Service()
options = Options()
options.add_experimental_option('detach', True)
chrome_browser = webdriver.Chrome(service=service, options=options)

# chrome_browser.maximize_window()
# selenium easy is no longer available so i'm using a demo from qafox
chrome_browser.get('https://omayo.blogspot.com/')


# == grab the title ==
# this shows that the title name is there and therefor True. if its not there it will be False
# print('omayo (QAFox.com)' in chrome_browser.title)

# an easier way to check our code is to use the assert keyword that comes with python. you do not see that much because if it returns False it will error out and exit out of the code
# assert 'omayo (QAFox.com)' in chrome_browser.title


# == grab something out of the body ==
# this will need the import for By

# because the normal methods are insufficient at locating what we want we'll have to use XPath at locating what we want
button = chrome_browser.find_element(By.CLASS_NAME, 'gsc-search-button')
# print(button)
print(button.get_attribute('innerHTML'))
print(button.get_attribute('value'))


# An XPath (XML Path Language) is a query language used to navigate and locate elements in an XML or HTML document. In Selenium, XPath is a powerful way to locate web elements in a DOM (Document Object Model) tree when other methods (like id, class, or name) are insufficient or not unique.
button_xpath = chrome_browser.find_element(
    By.XPATH, '//input[@class="gsc-search-button"]')
# print(button)
print(button_xpath.get_attribute('value'))


# == another button (using ID) ==
# button2 = chrome_browser.find_element(By.ID, 'but2')
# # print(button2)
# print(button2.get_attribute('innerHTML'))
