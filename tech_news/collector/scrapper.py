import requests
from time import sleep


def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=timeout)
    except:
        print("deu ruim mano")
        return ""
    else:
        if response.status_code != 200:
            return ''
        sleep(delay)
        return response.text
     


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""


if __name__ == '__main__':
    
    url = "https://httpbin.org/delay/10"
    print(fetch_content(url))

