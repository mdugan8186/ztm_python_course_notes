# ==== selenium basics 3 ====

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

service = Service()
options = Options()
options.add_experimental_option('detach', True)
chrome_browser = webdriver.Chrome(service=service, options=options)

# chrome_browser.maximize_window()
# selenium easy is no longer available so i'm using a demo from qafox
chrome_browser.get('https://omayo.blogspot.com/')


assert 'omayo (QAFox.com)' in chrome_browser.title


search_button = chrome_browser.find_element(
    By.XPATH, '//input[@class="gsc-search-button"]')
# print(search_button.get_attribute('value'))

assert 'Search' in chrome_browser.page_source

# getting a button through CSS
# a class will have a period (.) in front of it and an id will have a pound in front of it (#)
drop_box_button = chrome_browser.find_element(By.CSS_SELECTOR, '.dropbtn')
# print(drop_box_button.get_attribute('innerHTML'))

# it is a good idea to use sleep when automating. it is less likely for a browser to think you are a computer because of the delay
time.sleep(2)
# i have to use the XPath for this also
user_message = chrome_browser.find_element(
    By.XPATH, '//input[@class="gsc-input"]')
# print(user_message.get_attribute('value'))
user_message.clear()
# typing into a input box
user_message.send_keys('I AM EXTRA COOL')

# clicking a button
search_button.click()


# getting the output message
output_message = chrome_browser.find_element(By.TAG_NAME, 'b')
# print(output_message.text)

assert 'I AM EXTRA COOL' in output_message.text


# == closing the window ==
# sometimes you may have to use this command twice
# chrome_browser.close()

# this will also work to close the window
chrome_browser.quit()
