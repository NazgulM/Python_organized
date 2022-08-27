import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import pandas
import schedule
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

url = 'https://globus-online.kg/catalog/'
extra_url_meat = 'myaso_ptitsa_ryba/govyadina_baranina_farshi/'

response_meat = requests.get(url + extra_url_meat)
soup_meat = bs(response_meat.text, 'html.parser')
meat_names = soup_meat.find_all('div', 'list-showcase__name')
list_meat_names = [meat.text for meat in meat_names]

# for i in meat_names:
#     print(i.text)

price_meats = soup_meat.find_all('span', 'c-prices__value js-prices_pdv_ГЛОБУС Розничная')
price_meat_list = [int(price.text[:3]) for price in price_meats]
# print(price_meat_list)

# for i in price_meats:
#     print(i.text[:3])

# Grass
extra_url_zelen = 'ovoshchi_frukty_orekhi_zelen/zelen/'

response_zelen = requests.get(url + extra_url_zelen)
soup_zelen = bs(response_zelen.text, 'html.parser')
zelen_names = soup_zelen.find_all('div', 'list-showcase__name')
zelen_name_list = [zelen.text for zelen in zelen_names]
zelen_price = soup_zelen.find_all('span', 'c-prices__value js-prices_pdv_ГЛОБУС Розничная')

zelen_price_list = []
for i in zelen_price:
    price = ''
    for j in i.text:
        if j.isdigit():
            price += j
    zelen_price_list.append(int(price))
# print(zelen_price_list)


# sport items
extra_url_sport = 'tovary_dlya_sporta/'

response_sport = requests.get(url + extra_url_sport)
soup_sport = bs(response_sport.text, 'html.parser')
sport_prod_name = soup_sport.find_all('div', 'list-showcase__name')
# for i in sport_prod_name:
#     print(i.text)
sport_prod_list = [sport.text for sport in sport_prod_name]
sport_price = soup_sport.find_all('span', 'c-prices__value js-prices_pdv_ГЛОБУС Розничная')
sport_price_list = []
for i in sport_price:
    price = ''
    for j in i.text:
        if j == 'с':
            break
        else:
            price+=j
    sport_price_list.append(float(price))
print(sport_price_list)

prod_list_names = []
prod_list_price = []
prod_list_names = list_meat_names + zelen_name_list + sport_prod_list
# print(prod_list_names)
prod_list_price = price_meat_list + zelen_price_list + sport_price_list

prod_info = pd.DataFrame(
    {
       'Name of item': prod_list_names,
        'Price': prod_list_price
    }
)
print(prod_info)
prod_info.to_excel('prod_info.xlsx', index=False)

# Uploading to Google drive
folder = '19y95Rj7xq7kyj3qm8JwxlBmARqkGWA0s'
filepath = '/Users/naza/PycharmProjects/Python_Django/ParsingPython2022/Lesson4_ParsingGlobus'
file_excel = os.path.join(filepath, 'prod_info.xlsx')

excel_document_google = \
    drive.CreateFile({'parents': [{'id': folder}], 'title': 'prod_info.xlsx'})

excel_document_google.SetContentFile(file_excel)
excel_document_google.Upload()
print('File uploaded to Google Drive')
# 813792313796-rnof6o93v43s3u4lnu9bg139t2a8lmvd.apps.googleusercontent.com - client ID
# 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 - client secret
