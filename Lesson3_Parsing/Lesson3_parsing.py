from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import lxml

url = 'https://www.sciencenews.org/topic/animals/page/2'
response = requests.get(url)
soup = bs(response.text, 'html.parser')
articles = soup('div', {'class': 'post-item-river__content___2Ae_0'})
for i in articles:
    for article in articles:
        art_name = article.find_all('h3', class_='post-item-river__title___J3spU')
        for i in art_name:
            print(i.text.strip())

# pages = soup.find('nav', class_='pagination__wrapper___2qtdg')
# urls = []
# links = pages.find_all('a', class_='page-numbers')
#
# for link in links:
#     pageNum = 0
#     if link.text.isdigit():
#         int(link.text)
#     else:
#         pageNum = None
#     if pageNum != 0:
#         hrefText = link.get('href')
#         urls.append(hrefText)
#
# print(urls)
#
# for i in urls:
#     url = i
#     print(i)
