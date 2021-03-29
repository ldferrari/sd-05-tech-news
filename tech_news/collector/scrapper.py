import requests
import time


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        time.sleep(delay)

        if response.status_code != 200:
            return ""

        return response.text

    except requests.Timeout:
        return ""

    # def scrape(fetcher, pages=1):
