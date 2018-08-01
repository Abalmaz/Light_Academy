import lxml.html as html
import requests
# from urllib.request import urlopen


# page = html.parse(urlopen(main_domain_stat)).getroot()
#
# print(page)
#
# article_links = page.xpath('//li/article[contains(@class, "post_preview")]/h2[@class="post__title"]/'
#                            'a[@class="post__title_link"]/@href')
#
# print(article_links)

main_domain_stat = 'https://habr.com'
req = requests.get(main_domain_stat)
page = html.fromstring(req.content)

# print(page)

article_texts = page.xpath('//li/article[contains(@class, "post_preview")]/div[contains(@class, "post__body")]')

# print(article_texts)

for article in article_texts:
    print('**********')
    # art_text = article.xpath('div[contains(@class, "post__text")]//text()')
    art_text = article.xpath('.//text()')
    print(art_text)
