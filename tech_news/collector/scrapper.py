import requests
import time


def fetch_content(url, timeout=3, delay=0.5):
    """Realiza uma requisição HTTP e retorna conteúdo como resposta."""

    try:
        response = requests.get(url, timeout=timeout)
        time.sleep(delay)

        if response and response.status_code != 200:
            return ''

        return response.text

    except requests.Timeout:
        return ''


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
