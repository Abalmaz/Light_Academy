from bs4 import BeautifulSoup
import requests

url = 'https://habr.com'

req = requests.get(url)

soup = BeautifulSoup(req.content, 'html.parser')
article_list = soup.select('li article.post h2 a')

for article in article_list:
    print(article['href'])