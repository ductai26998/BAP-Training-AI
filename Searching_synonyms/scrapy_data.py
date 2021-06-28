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

