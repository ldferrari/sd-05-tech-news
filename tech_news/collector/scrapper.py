import requests
import time
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    response = requests.get(url, timeout=timeout)
    time.sleep(delay)
    success_status = 200
    if response.status_code != success_status:
        return ""
    return response.text


def scrape(fetcher, pages=1):
    actual_page = 1
    results = []
    while actual_page <= pages:
        main_url = "https://www.tecmundo.com.br/novidades?page=" + str(
            actual_page
        )
        response = fetcher(main_url)
        selector = Selector(text=response)
        news_urls = selector.css(
            ".tec--list--lg h3 a.tec--card__title__link::attr(href)"
        ).getall()
        print(news_urls)
        for url in news_urls:
            response_new = fetcher(url, 3, 1)
            selector_new = Selector(text=response_new)
            title = selector_new.css(
                "h1.tec--article__header__title::text"
            ).get()
            timestamp = selector_new.css(
                ".tec--timestamp__item time::attr(datetime)"
            ).get()
            writer = selector_new.css(
                "div.tec--author__info a.tec--author__info__link::text"
            ).get()
            shares_count = selector_new.css("div.tec--toolbar__item::text").re(
                r"\d"
            )
            comments_count = selector_new.css(
                "div.tec--toolbar__item button.tec--btn::attr(data-count)"
            ).get()
            summary = selector_new.css(
                "div.tec--article__body p:first-child *::text"
            ).getall()
            sources = selector_new.css(
                "div.tec--author__info p.z--m-none a.tec--link::text"
            ).getall()
            categories = selector_new.css(
                "div.z--px-16 div.js-categories a::text"
            ).getall()

            try:
                share_count = int("".join(shares_count))
            except Exception:
                share_count = 0
            try:
                comments_count = int(comments_count)
            except Exception:
                comments_count = 0
            try:
                summary = "".join(summary)
            except Exception:
                summary = ""

            new_result = {
                "url": url,
                "title": title,
                "timestamp": timestamp,
                "writer": writer,
                "shares_count": share_count,
                "comments_count": comments_count,
                "summary": summary,
                "sources": sources,
                "categories": categories,
            }
            print(summary)
            results.append(new_result)
        actual_page += 1

    print(results)
    return results
