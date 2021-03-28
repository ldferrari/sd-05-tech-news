import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
    except requests.RequestException:
        print("Oops!  That was no valid number.  Try again...")
        return ''
    else:
        if response.status_code != 200:
            return ''
        sleep(delay)
        return response.text


def news(url, selector):
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = selector.css("a.tec--author__info__link::text").get()
    shares_count = selector.css(".tec--toolbar__item::text").re_first(r'\d') or "0"
    comments_count = selector.css("#js-comments-btn::attr(data-count)").re_first(r'\d') or "0"
    summary = selector.css(".tec--article__body p::text").get()
    sources = selector.css(".z--mb-16 a::text").getall()
    categories = selector.css("#js-categories a::text").getall()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


def scrape(fetcher, pages=1):
    url = "https://www.tecmundo.com.br/novidades"
    news_list = []
    for page in range(1, pages + 1):
        selector = Selector(fetcher(f"{url}?page={page}"))
        all_url = selector.css(
            ".tec--list__item .tec--card__title__link::attr(href)"
        ).getall()
        for url in all_url:
            selector = Selector(fetcher(url))
            news_list.append(news(url, selector))
    return news_list
