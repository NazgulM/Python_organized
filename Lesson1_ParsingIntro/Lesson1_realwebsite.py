from bs4 import BeautifulSoup
import requests

url = 'https://avangardstyle.kg/builds/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
buildings = soup.find_all('div', class_='object-card_title')
building_descr = soup.find_all('div', class_='object-card_desc')

building_list = [building.text for building in buildings]
print(building_list)

building_desc_list = [descr.text.strip() for descr in building_descr]
print(building_desc_list)

building_avg = dict(zip(building_list, building_desc_list))

for name_build, descr in building_avg.items():
    print(f'Name of the complex: {name_build}'
          f'\nDescription: {descr}\n')
