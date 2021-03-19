import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
    except requests.Timeout:
        return ''
    else:
        if (response.status_code != 200):
            return ''
        sleep(delay)
        return response.text


def scrape(fetcher, pages=1):
    page = Selector(text=fetcher)
    url = page.css('head link::attr(href)')[20].get()
    print(url)
