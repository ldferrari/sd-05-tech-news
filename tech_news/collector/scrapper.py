import requests
import time


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        time.sleep(delay)
    except OSError:
        return ""
    else:
        return response.text


def scrape(fetcher, pages=1):
    try:
        response = requests.get(fetcher)
    except OSError:
        return ""
    else:
        return response.text
