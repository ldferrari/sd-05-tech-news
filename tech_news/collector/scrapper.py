import requests
import time
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
    except requests.Timeout:
        return ""
    else:
        if response.status_code != 200:
            return ""
        time.sleep(delay)
        return response.text


def scrape(fetcher, pages=1):
    noticias = []

    for page in range(pages):
        URL_BASE = "https://www.tecmundo.com.br/novidades"
        page_url = f"?page={page}"
        full_url = URL_BASE + page_url
        selector = Selector(text=fetcher(full_url))

        for url in selector.css(".tec--list__item h3 a::attr(href)").getall():
            selector_new = Selector(text=fetcher(url))
            title = selector_new.css(
                ".tec--article__header__title::text"
            ).get()
            timestamp = selector_new.css(
                "#js-article-date ::attr(datetime)"
            ).get()
            writer = selector_new.css(".tec--author__info__link ::text").get()
            shares_count_str = selector_new.css(
                    "div.tec--toolbar__item:nth-child(1)::text"
                ).re_first(r"[0-9]+")
            print(f"shares count is :{shares_count_str}")
            shares_count = int(shares_count_str)
            comments_count_str = selector_new.css(
                "#js-comments-btn::text").re_first(r"[0-9]+")
            print(f"comments count is :{comments_count_str}")
            comments_count = int(comments_count_str)
            summary = selector_new.css(".tec--article__body *::text").get()
            sources = selector_new.css(".z--mb-16 a::text").getall()
            categories = selector_new.css(
                "a.tec--badge--primary::text"
            ).getall()

            noticias.append(
                {
                    "url": url,
                    "title": title,
                    "timestamp": timestamp,
                    "writer": writer,
                    "shares_count": shares_count,
                    "comments_count": comments_count,
                    "summary": summary,
                    "sources": sources,
                    "categories": categories,
                }
            )
    return noticias
