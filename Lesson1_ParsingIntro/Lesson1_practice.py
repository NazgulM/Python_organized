from bs4 import BeautifulSoup
import requests

url = 'http://sport.akipress.org/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('div', class_='feed-title')
article_descr = soup.find_all('div', class_='feed-content')

article_list = [article.text.strip() for article in articles]
print(article_list)

article_desc_list = [descr.text.strip() for descr in article_descr]
print(article_desc_list)

