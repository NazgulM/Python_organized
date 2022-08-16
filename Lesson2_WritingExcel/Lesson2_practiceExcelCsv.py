from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

url = 'http://www.stat.kg/ru/opendata/category/855/'
response = requests.get(url)
soup = bs(response.text, 'html.parser')

table = soup.find('table')
td = table.find_all('td')

data = []
for i in td:
    data.append(i.text.strip())

print(data)


df = pd.DataFrame({'List of KG students ': data})

df.to_csv('listKg.csv')
df.to_excel('listKg.xlsx')
