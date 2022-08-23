from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

url = 'https://www.nytimes.com/interactive/2021/world/covid-vaccinations-tracker.html'
response = requests.get(url)
soup = bs(response.text, 'html.parser')

table = soup.find('table')
td = table.find_all('td')

data = []
for i in td:
    data.append(i.text.strip())

print(data)

df = pd.DataFrame({'List of vaccinated countries ': data})

df.to_csv('vaccination.csv')
df.to_excel('vaccination.xlsx')