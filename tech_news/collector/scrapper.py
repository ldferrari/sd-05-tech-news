import requests
import time


def fetch_content(url, timeout=3, delay=0.5):

    try:
        response = requests.get(url, timeout=timeout)

    except requests.ReadTimeout:
        time.sleep(delay)
        response = requests.get(url, timeout=timeout)
    finally:
        if response.status_code and response.status_code == 200:
            print(response)
            print(response.status_code)
        else:
            print(response)
            print('')


fetch_content("https://app.betrybe.com/")
# fetch_content("https://httpbin.org/status/404")

def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
