import requests
import time
import pytest
import re
from parsel import Selector

URL_BASE = "https://www.tecmundo.com.br/novidades"


def fetch_content(url, timeout=3, delay=0.5):

    try:
        response = requests.get(url, timeout=timeout)

    except requests.ReadTimeout:
        # print("readTImeout")
        return ""

    if response.status_code and response.status_code == 200:
        # print(response)
        time.sleep(delay)
        # print('returning response text')
        return response.text

    else:
        return ""


def scrape(fetcher, pages=1): 
    list_news = []
    page = 1 

    while page <= pages:
        response_text = fetcher(URL_BASE + "?page={page}")
        # print(response_text)
        selector = Selector(text=response_text)
        # porra = selector.css(".tec--list__item h3 a::attr(href)").getall()
        # print(porra) 

        for url in selector.css(".tec--list__item h3 a::attr(href)").getall():
            print(page)
            # print(url)
            selector_url = Selector(text=fetcher(url))
            # print(selector_url)
            title = selector_url.css(".tec--article__header__title::text").get()
            # print(title)

            # timestamp = selector_url.css("#js-article-date ::attr(datetime)").get().strip()
            # # print(timestamp)

            # author = selector_url.css(".tec--author__info__link ::text").get().strip()
            # # print(author)

            # shares_count_dirty = selector_url.css(".tec--toolbar__item ::text").getall()[3]
            # shares_count = [int(i) for i in shares_count_dirty.split() if i.isdigit()][
            #     0
            # ]
            # # print(shares_count)

            # comments_count_dirty = selector_url.css(".tec--toolbar__item ::text").getall()[
            #     8
            # ]
            # comments_count = [
            #     int(i) for i in comments_count_dirty.split() if i.isdigit()
            # ][0]
            # # print(comments_count)

            # summary_list = selector_url.css(".p402_premium > p *::text").getall()
            # summary = "".join([str(elem) for elem in summary_list])
            # # print(summary)

            # sources = selector_url.css(".tec--badge *::text").get().strip()
            # # print(sources)

            # categories_dirty = selector_url.css("#js-categories > a *::text").getall()
            # categories = [elem.strip() for elem in categories_dirty]
            # # print(categories)

            list_news.append(
                {
                    "url": url,
                    "title": title,
                    # "timestamp": timestamp,
                    # "writer": author,
                    # "shares_count": shares_count,
                    # "comments_count": comments_count,
                    # "summary": summary,
                    # "sources": [sources],
                    # "categories": categories,
                }
            )
        page += 1
    return list_news
    

print(scrape(fetcher=fetch_content, pages=2)[1])
