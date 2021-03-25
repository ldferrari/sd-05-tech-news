import requests
from parsel import Selector
from time import sleep


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
    except requests.ReadTimeout:
        # ?response.status_code == '200':
        return ''
    else:
        if response.status_code != 200:
            return ''
        # return Selector(text=response.text)
        sleep(delay)
        return response.text


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
    result = []
    for page in range(pages):
        base_url = "https://www.tecmundo.com.br/novidades"
        page_url = f"?page={page}"
        the_url = base_url + page_url
        selector = Selector(text=fetcher(the_url))
        for url in selector.css(".tec--list__item h3 a::attr(href)").getall():
            new_selector = parsel.Selector(text=fetcher(url))
            title = new_selector.css(
                ".tec--article__header__title::text"
                ).get()
            timestamp = new_selector.css(
                "#js-article-date ::attr(datetime)"
            ).get()
