import requests
from time import sleep


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        if (response.status_code != 200):
            return ''
        sleep(delay)
        return response.text
    except OSError:
        print('Deu algum erro')
        return ''


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
