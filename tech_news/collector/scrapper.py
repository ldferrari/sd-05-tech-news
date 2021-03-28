import requests
from time import sleep


def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except requests.Timeout:
        return ""
    else:
        return response.text


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
