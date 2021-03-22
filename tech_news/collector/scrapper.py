import requests
# from parsel import Selector
from time import sleep


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
    except requests.ReadTimeout:
        # ?response.status_code == '200':
        return ''
    else:
        if response.status_code != 200:
            return ''
        # return Selector(text=response.text)
        return response.text
    finally:
        sleep(delay)


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
