# $ pip install requests BeautifulSoup4 lxml pandas
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = 'https://guide.michelin.com/th/en/bangkok-region/bangkok/restaurants/online-reservation'
response = requests.get(url)
html_code = response.text

soup = bs(html_code, 'html.parser')
all_menu = soup.find('div', class_='row restaurant__list-row js-restaurant__list_items')
menu_divs = all_menu.find_all('div', class_='card__menu-content js-match-height-content')  # Ищем элемент div с классом 'container'
#title_tag = container_div2.find_all('h3', class_='card__menu-content--title')
with open('output.txt', 'w') as file:
	for menu_div in menu_divs:
		h3_tags = menu_div.find_all('h3')
		for h3_tag in h3_tags:
			dish_name = h3_tag.text
			file.write(dish_name + '\n')
   