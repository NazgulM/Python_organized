from bs4 import BeautifulSoup
import requests

url = 'https://ecostan.kg/biotop/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.find_all('div', class_='entry-title')
title_list = []

for i in title:
    title_list.append(i.text.strip())
print(title_list)

title_content = soup.find_all('div', class_='post-box__content')
title_content_list = []

print(title_content)