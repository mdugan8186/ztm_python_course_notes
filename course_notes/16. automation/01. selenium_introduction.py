# ==== selenium introduction ====

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Use the default system PATH for ChromeDriver
service = Service()  # No need to specify the executable_path
# Path to your ChromeDriver executable if chromedriver IS NOT in your home path
# service = Service(executable_path='./chromedriver')

# Chrome options
options = Options()
options.add_experimental_option('detach', True)  # Keeps the browser open

# Initialize the browser
chrome_browser = webdriver.Chrome(service=service, options=options)

# Open a webpage
# chrome_browser.get("https://www.google.com")
# if you do not use the chrome_browser.get you will just get a blank window

# Print the browser instance
# print(chrome_browser)

# chrome_browser.maximize_window()

# chrome_browser
