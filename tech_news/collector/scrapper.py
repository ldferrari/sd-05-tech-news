import requests
from time import sleep


def fetch_content(url, timeout=3, delay=0.5):
    try:
        RESPONSE = requests.get(url, timeout=timeout)
        sleep(delay)
    except requests.ReadTimeout:
        return ""
    else:
        return RESPONSE.text


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
