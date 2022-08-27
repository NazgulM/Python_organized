from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import lxml

url = 'https://scrapingclub.com/exercise/list_basic/?page='
response = requests.get(url)
soup = bs(response.text, 'html.parser')
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
for k,v in enumerate(items, start=1):
    prod_name = v.find('h4', class_='card-title').text.strip()
    prodPrice = v.find('h5').text.strip()

    print(f'{k}: {prod_name} --- Price: {prodPrice}')

ul_page = soup.find('ul', class_='pagination')
urls_list = []
links = ul_page.find_all('a', class_='page-link')
for i in links:
    pageNum = 0
    if i.text.isdigit():
        int(i.text)
    else:
        pageNum = None

    if pageNum is not None:
        hrefLink = i.get('href')
        urls_list.append(hrefLink)
counter = 2;
for i in urls_list:
    new_url = url.replace('?page=1', i)
    response = requests.get(new_url)
    soup = bs(response.text, 'html.parser')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    print(f'=======Page {counter}=======')
    for k, v in enumerate(items, start=1):
        prod_name = v.find('h4', class_='card-title').text.strip()
        prodPrice = v.find('h5').text.strip()

        print(f'{k}: {prod_name} --- Price: {prodPrice}')
    counter+=1;
