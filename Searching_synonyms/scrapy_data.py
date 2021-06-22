# # from selenium import webdriver
# # from BeautifulSoup import BeautifulSoup
# # import pandas as pd
# #
# # driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
# #
# # ratings=[] #List to store rating of the product
# # driver.get('<a href="https://www.thesaurus.com/browse">https://www.thesaurus.com/browse</a>')
# #
# # content = driver.page_source
# # soup = BeautifulSoup(content)
# # for a in soup.findAll('a',href=True, attrs={'class':'eh475bn0'}):
# #     name=a.find('div', attrs={'class':'_3wU53n'})
# #     price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
# #     rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
# #     products.append(name.text)
# #     prices.append(price.text)
# #     ratings.append(rating.text)
# #
# # df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings})
# # df.to_csv('products.csv', index=False, encoding='utf-8')
#
#
# import scrapy
#
#
# class BrickSetSpider(scrapy.Spider):
#     """
#     name = "brickset_spider"
#     start_urls = ['https://www.thesaurus.com/browse/look']
#     def parse(self, response):
#         SET_SELECTOR = '#meanings .e1ccqdb60 li'
#         for brickset in response.css(SET_SELECTOR):
#             NAME_SELECTOR = 'a ::text'
#             yield {
#                 'word': brickset.css(NAME_SELECTOR).extract()[0],
#             }
#
#         # NEXT_PAGE_SELECTOR = '.rc-pagination-next a ::attr(href)'
#         # next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
#         # if next_page:
#         #     yield scrapy.Request(
#         #         response.urljoin(next_page),
#         #         callback=self.parse
#         #     )
#     """
#     name = "brickset_spider"
#     start_urls = ['https://www.ef-australia.com.au/english-resources/english-vocabulary/top-3000-words/']
#
#     def handle(list):
#         return map(lambda element: element[4:] if element != 'a' else element, list)
#
#     def parse(self, response):
#         SET_SELECTOR = '.field-item'
#         for brickset in response.css(SET_SELECTOR):
#             NAME_SELECTOR = 'p:last-child ::text'
#             yield {
#                 'words': brickset.css(NAME_SELECTOR).extract(),
#             }

import requests
from bs4 import BeautifulSoup

def scrape(url: str, selector: str):
    """
        scrape data from a web page
        input:
            url: url of the web page
            selector: CSS selector
        return: list | data which you scraped
    """
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    data = []
    if soup.select_one(selector):
        data = soup.select_one(selector).get_text(strip=True, separator=",").split(",")
    return data

