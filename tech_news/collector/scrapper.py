import requests


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get('https://www.tecmundo.com.br/novidades')
        if (response.status_code != 200):
            return ''
        return response.text
    except OSError:
        print('Deu algum erro')


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
