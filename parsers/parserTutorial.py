# $ pip install requests BeautifulSoup4 lxml pandas
import requests
from bs4 import BeautifulSoup as BS
import pandas as pd

# Получить страничку 
url = 'https://www.franksonnenbergonline.com/blog/are-you-grateful/'
response = requests.get(url) #TODO: В этой строке кода отправляется GET-запрос к указанному URL-адресу с помощью функции get() из библиотеки requests. Ответ на запрос сохраняется в переменной response.
response.raise_for_status() #TODO: Эта строка кода проверяет статус ответа на запрос. Если статус не является успешным (не в диапазоне 200-299), то вызывается исключение HTTPError, которое сообщает об ошибке соединения или недопустимом статусе ответа.

# Парсинг названия поста
soup = BS(response.text, 'lxml') #TODO: Создается объект BeautifulSoup, используя содержимое ответа response.text и парсер lxml.
title_tag = soup.find('main').find('header').find('h1') #TODO: Используя метод find() объекта soup, ищется элемент main, затем внутри него ищется элемент header, а внутри него - элемент h1. Результат сохраняется в переменной title_tag.
title_text = title_tag.text #TODO: Затем, из найденного элемента h1 извлекается текст с помощью метода text() и сохраняется в переменной title_text.
print(title_text)

# Парсинг Картинки
soup = BS(response.text, 'lxml') 
title_tag = soup.find('img', class_='attachment-post-image') ['src'] #TODO: Тот же .find(), только указали параметр class_. Нижнее подчёркивание разработчики библиотеки добавили для того, чтобы не было пересечения со словом class из Python, которое используется для создания классов.
print(title_tag) #TODO: Осталось достать адрес картинки, он лежит в аргументе src:

# Парсинг поста
soup = BS(response.text, 'lxml') 
title_tag = soup.find('div', class_='entry-content')#.find('header').find('h1')
title_text = title_tag.text 
print(title_text)

#! Получение html страницы
url = 'https://www.example.com'  # Замените на нужный URL-адрес
response = requests.get(url)  # Отправляем GET-запрос на указанный URL-адрес
html_code = response.text  # Получаем HTML-код страницы

#! Получение данных - методы
#? Поиск элементов по тегу

 html_code = '<html><body><h1>Title</h1><p>Paragraph</p></body></html>'

 soup = BeautifulSoup(html_code, 'html.parser')  # Создаем объект BeautifulSoup
 title_tag = soup.find('h1')  # Ищем первый элемент с тегом 'h1'
 title_text = title_tag.text  # Получаем текст элемента

 print(title_text)  # Выводит: Title

#? Поиск элементов по классу

html_code = '<div class="container"><h1>Title</h1><p>Paragraph</p></div>'

soup = BeautifulSoup(html_code, 'html.parser')
container_div = soup.find('div', class_='container')  # Ищем элемент div с классом 'container'
title_tag = container_div.find('h1')  # Ищем элемент h1 внутри найденного div
title_text = title_tag.text

print(title_text)  # Выводит: Title

#? Поиск элементов по идентификатору

html_code = '<div id="content"><h1>Title</h1><p>Paragraph</p></div>'

soup = BeautifulSoup(html_code, 'html.parser')
content_div = soup.find(id='content')  # Ищем элемент с идентификатором 'content'
title_tag = content_div.find('h1')  # Ищем элемент h1 внутри найденного div
title_text = title_tag.text

print(title_text)  # Выводит: Title

#? Использование метода find_all() для поиска нескольких элементов

html_code = '<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>'

soup = BeautifulSoup(html_code, 'html.parser')
list_items = soup.find_all('li')  # Ищем все элементы с тегом 'li'

for item in list_items:
    print(item.text)  # Выводит: Item 1, Item 2, Item 3


#! Сохранение данных парса

#? Сохранение данных в файл
with open('output.txt', 'w') as file:
    file.write(title_text)
    
#? Фильтрация и обработка данных
soup = BeautifulSoup(html_code, 'html.parser')
list_items = soup.find_all('li')

filtered_items = [item.text.upper() for item in list_items]  # Преобразование элементов в верхний регистр

print(filtered_items)  # Выводит: ['ITEM 1', 'ITEM 2', 'ITEM 3']

#? Сохранение данных в базу данных
soup = BeautifulSoup(html_code, 'html.parser')
title_tags = soup.find_all('h1')

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS titles (title TEXT)')  # Создание таблицы в базе данных

for title_tag in title_tags:
    title_text = title_tag.text
    cursor.execute('INSERT INTO titles VALUES (?)', (title_text,))  # Вставка данных в таблицу

conn.commit()  # Сохранение изменений
conn.close()
# В этом примере мы сохраняем заголовки веб-страницы в базу данных SQLite, создавая таблицу "titles" и вставляя данные в нее

#? Обработка данных в словарь
soup = BeautifulSoup(html_code, 'html.parser')
table_rows = soup.find_all('tr')

data = {}

for row in table_rows:
    key = row.find('td').text
    value = row.find_all('td')[1].text
    data[key] = value

print(data)  # Выводит: {'Key 1': 'Value 1', 'Key 2': 'Value 2'}
#В этом примере мы обрабатываем данные таблицы HTML и сохраняем их в словарь, используя значения первого столбца в качестве ключей и значения второго столбца в качестве значений

#! Функция под вывод массива 
soup = BeautifulSoup(html_code, 'html.parser')
menu_divs = soup.find_all('div', class_='menu')

for menu_div in menu_divs:
    h3_tags = menu_div.find_all('h3')
    for h3_tag in h3_tags:
        dish_name = h3_tag.text
        print(dish_name)
        
#TODO: Работающий код на пару желемнтов див и сохранение в файл тхт
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
#TODO: Конец