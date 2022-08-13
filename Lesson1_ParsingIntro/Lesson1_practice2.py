from bs4 import BeautifulSoup
import requests

url = 'https://sport.akipress.org/category:181'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

title_news = soup.find_all('div', class_='category-feed-title')
news_title_list = []

# for title in title_news:
#     news_title_list.append(soup.find_all('a'))

for i in title_news:
    news_title_list.append(i.text.strip())

# for i in news_title_list:
#     print(i)

title_news_content = []
# for i in news_title_list:
#     title_news_content.append(i.split('\n'))

for i in news_title_list:
    temp_list = i.split('\n')
    title_news_content.append(temp_list[0])

for num, title in enumerate(title_news_content, 1):
    print(f'{num} -- {title}')