# Referências:
# https://stackoverflow.com/questions/19342111/get-http-error-code-from-requests-exceptions-httperror

import requests
from time import sleep


def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=timeout)
    except (requests.ReadTimeout, requests.HTTPError):
        return ""
    else:
        return response.text
    finally:
        sleep(delay)


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
