import requests
import time


def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=timeout)
    except requests.Timeout:
        return ''
    else:
        if (response.status_code != 200):
            return ''
        time.sleep(delay)
        return response.text

# https://requests.readthedocs.io/en/master/user/advanced/#timeouts
# https://realpython.com/python-sleep/


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
