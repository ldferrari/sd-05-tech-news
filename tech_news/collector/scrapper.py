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
        for url in news_urls:
            response_new = fetcher(url, 3, 1)
            selector_new = Selector(text=response_new)
            build_scrap = builder(selector_new)
            corrected_scrap = correction(
                build_scrap["shares_count"],
                build_scrap["comments_count"],
                build_scrap["summary"],
            )

            new_result = {
                "url": url,
                "title": build_scrap["title"],
                "timestamp": build_scrap["timestamp"],
                "writer": build_scrap["writer"],
                "shares_count": corrected_scrap["shares_count"],
                "comments_count": corrected_scrap["comments_count"],
                "summary": corrected_scrap["summary"],
                "sources": build_scrap["sources"],
                "categories": build_scrap["categories"],
            }
            results.append(new_result)
        actual_page += 1

    return results


def correction(shares_count, comments_count, summary):
    if shares_count != "None":
        shares_count = int("".join(shares_count))
    else:
        shares_count = 0
    if comments_count != "None":
        comments_count = int(comments_count)
    else:
        comments_count = 0
    if summary != "":
        summary = "".join(summary)

    return {
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
    }


def builder(selector_new):
    title = selector_new.css("h1.tec--article__header__title::text").get()
    timestamp = selector_new.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()
    writer = selector_new.css(
        "div.tec--author__info a.tec--author__info__link::text"
    ).get()
    shares_count = selector_new.css("div.tec--toolbar__item::text").re(r"\d")
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

    return {
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }
