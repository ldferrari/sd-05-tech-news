import requests
from time import sleep


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
    except requests.ReadTimeout:
        return ""
    else:
        code_success = 200
        if response.status_code != code_success:
            return ""
        return response.text

    finally:
        sleep(delay)


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
