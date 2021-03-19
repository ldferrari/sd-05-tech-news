import requests
import time
import pytest
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):

    try:
        response = requests.get(url, timeout=timeout)

    except requests.ReadTimeout:
        print("readTImeout")
        return ""

    if response.status_code and response.status_code == 200:
        print(response)
        time.sleep(delay)
        return response.text

    else:
        return ''


# fetch_content("https://app.betrybe.com/")
# fetch_content("https://httpbin.org/status/404")
# fetch_content("https://httpbin.org/delay/10")

URL_BASE = "https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm"

def scrape(fetcher, pages=1):
    response_text = fetcher(URL_BASE)
    selector = Selector(response_text)

    title =