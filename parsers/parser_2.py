# $ pip install requests BeautifulSoup4 lxml pandas

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = 'https://www.sports.ru/tribuna/'
response = requests.get(url)
html_code = response.text

soup = bs(html_code, 'html.parser' )
all_menu = soup.find('div', class_='tabs__body')
menu_divs = all_menu.find_all('div', class_='tabs__panel tabs__panel_active')  # Ищем элемент div с классом 'container'
#title_tag = container_div2.find_all('h3', class_='card__menu-content--title')
with open('output.txt', 'w', encoding='utf-8') as file:
	for menu_div in menu_divs:
		h3_tags = menu_div.find_all('a')
		for h3_tag in h3_tags:
			dish_name = h3_tag.text
			file.write(dish_name + '\n')
	for menu_div in menu_divs:
		h3_tags = menu_div.find_all('time', class_='time-block time-block_top')
		for h3_tag in h3_tags:
			dish_name = h3_tag.text
			file.write(dish_name + '\n')
	for menu_div in menu_divs:
		h3_tags = menu_div.find_all('span', class_='voting__info-count')
		for h3_tag in h3_tags:
			dish_name = h3_tag.text
			file.write(dish_name + '\n')