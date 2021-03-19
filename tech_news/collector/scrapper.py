import requests
import time
import pytest
import re
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):

    try:
        response = requests.get(url, timeout=timeout)

    except requests.ReadTimeout:
        # print("readTImeout")
        return ""

    if response.status_code and response.status_code == 200:
        # print(response)
        time.sleep(delay)
        return response.text

    else:
        return ""


# fetch_content("https://app.betrybe.com/")
# fetch_content("https://httpbin.org/status/404")
# fetch_content("https://httpbin.org/delay/10")


def scrape(fetcher, pages=1):
    response_text = fetcher

    print(response_text)

    selector = Selector(response_text)

    url = selector.css("#js-article-title ::text").get().strip()

    title = selector.css("#js-article-title ::text").get().strip()
    # print(title)

    timestamp = selector.css("#js-article-date ::attr(datetime)").get().strip()
    # print(timestamp)

    author = selector.css(".tec--author__info__link ::text").get().strip()
    # print(author)

    shares_count_dirty = selector.css(".tec--toolbar__item ::text").getall()[3]
    shares_count = [int(i) for i in shares_count_dirty.split() if i.isdigit()][
        0
    ]
    # print(shares_count)

    comments_count_dirty = selector.css(".tec--toolbar__item ::text").getall()[
        8
    ]
    comments_count = [
        int(i) for i in comments_count_dirty.split() if i.isdigit()
    ][0]
    # print(comments_count)

    summary_list = selector.css(".p402_premium > p *::text").getall()
    summary = "".join([str(elem) for elem in summary_list])
    # print(summary)

    sources = selector.css(".tec--badge *::text").get().strip()
    # print(sources)

    categories_dirty = selector.css("#js-categories > a *::text").getall()
    categories = [elem.strip() for elem in categories_dirty]
    # print(categories)

    return [
        {
            "url": ????????????????????????/,
            "title": title,
            "timestamp": timestamp,
            "writer": author,
            "shares_count": shares_count,
            "comments_count": comments_count,
            "summary": summary,
            "sources": [sources],
            "categories": categories,
        }
    ]

URL_BASE = "https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm"


print(scrape(fetcher=fetch_content(URL_BASE), pages=2))
