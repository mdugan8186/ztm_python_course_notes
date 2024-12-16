# ==== BeautifulSoup selectors ====

import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.select('a'))
# print(soup.select('div'))
# print(soup.select('.score'))  # . stands for class
# print(soup.select('#score_42429197')) # # stands for ID
# print(soup.select('#score_42429197'))
# print(soup.select('.titleline'))
links = soup.select('.titleline')
votes = soup.select('.score')
# print(votes[0])
# print(votes[0].get('id'))
