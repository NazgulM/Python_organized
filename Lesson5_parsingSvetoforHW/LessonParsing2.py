import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import schedule
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

gauth = GoogleAuth()
drive = GoogleDrive(gauth)
url = 'https://svetofor.info/tehnika-dlya-doma/'
response = requests.get(url)

soup = bs(response.text, 'html.parser')

name_goods = soup.find_all('div', class_='ty-grid-list__item-name')
prices = soup.find_all('span', attrs={"class": "ty-price-num"})

nameList = [tovar.text.strip() for tovar in name_goods]
priceList = []
for i in prices:
    if i.text == 'с':
        continue
    priceList.append(int(i.text))

for page in range(2, 93):
    extra_url = f'page-{page}/'
    response = requests.get(url + extra_url)
    soup = bs(response.text, 'html.parser')
    name_goods = soup.find_all('div', class_='ty-grid-list__item-name')
    prices = soup.find_all('span', attrs={"class": "ty-price-num"})

    # print(f'*********Page number: {page}**********')
    for n in name_goods:
        nameList.append(n.text.strip())

    for i in prices:
        if i.text == 'с':
            continue
        priceList.append(int(i.text))

# Дальше запись в Экзель и загрузка в Гугл драйв

df = pd.DataFrame(list(zip(nameList, priceList)), columns=['Name of goods', 'Price'])

df.to_excel('goods_info.xlsx', index=False)
print('Excel file uploaded')

# Uploading to Google Drive
folder = '19y95Rj7xq7kyj3qm8JwxlBmARqkGWA0s'
filepath = '/Users/naza/PycharmProjects/Python_Django/ParsingPython2022/Lesson5_parsingSvetoforHW'
file_excel = os.path.join(filepath, 'goods_info.xlsx')
excel_document_google = drive.CreateFile({'parents': [{'id': folder}], 'title':'Goods_info.xlsx'})
excel_document_google.SetContentFile(file_excel)
excel_document_google.Upload()
print('File uploaded to Google drive')