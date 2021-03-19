import requests
import time
def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqui"""
        response = requests.get(url, timeout)
        if response.status_code != 200:
            return ''
        return response


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
