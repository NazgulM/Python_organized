from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

url = 'https://www.worldometers.info/coronavirus/country/kyrgyzstan/'
response = requests.get(url)
soup = bs(response.text, 'html.parser')

div_cases = soup.find_all('div', class_='maincounter-number')
# print(div_cases)

data = []
for case in div_cases:
    span = case.find('span')
    data.append(span.string)

# print(data)

df = pd.DataFrame({'CoronaData for KG ': data})
df.index = ['Total Case', 'Death', 'Recovered']

df.to_csv('CoronaData.csv')
df.to_excel('CoronaDataKg.xlsx')
