from bs4 import BeautifulSoup
import requests

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_= 'author')
list_quotes = []
author_list = []

for quote in quotes:
    list_quotes.append(quote.text)
print(list_quotes)

for num, quote in enumerate(list_quotes, 1):
    print(f'{num} - {quote}')

print('*' * 20)

for num, author in enumerate(author_list, 1):
    print(f'{num} - {author}')