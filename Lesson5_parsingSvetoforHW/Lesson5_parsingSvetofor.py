import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import pandas
import schedule
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

website = 'https://svetofor.info/tehnika-dlya-doma'
response = requests.get(website)
# print(response.status_code)
soup = bs(response.content, 'html.parser')
# print(soup)
items = soup.find_all('div', class_='ty-grid-list__item-name')
item = soup.find_all('a', 'product-title')
print(str(item))
# pages = list(range(1, 106))
# for page in pages:
#     response = requests.get('https://svetofor.info/tehnika-dlya-doma?page={}'.format(page)).text
#     soup = bs(response, 'html.parser')
#     # print(soup.prettify())
# items = soup.find_all('div', class_='ty-column4')
# print(len(items))
# items_list = []
# for i in range(len(items)):
#     items_list.append(items[i].text)
# print(len(items_list))
# prod_info = pd.DataFrame(
#     {
#        'Name of item': items_list,
#     }
# )
# prod_info.to_excel('prod_info.xlsx', index=False)

# for k,v in enumerate(items, start=1):
#     prodName = v.find('a', 'product-title').text
#     # print(prodName)
# prices = soup.find_all('div', 'ty-grid-list__price')
# for k,v in enumerate(prices, start=1):
#     prodPrices = v.find('span', 'ty-price-num').text
