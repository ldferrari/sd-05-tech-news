import requests
import time


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(delay)
    except requests.ReadTimeout:
        response = requests.get(url, timeout=3)
    finally:
        if (response.status_code != 200):
            return ''
    return response


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
