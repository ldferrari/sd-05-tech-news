import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        # tem que passar timeout=timeout por causa do parametro nomeavel
        # se nao fizer a importação usando o from dá errado =( 
        sleep(delay)
        response = requests.get(url, timeout=timeout)
    except requests.exceptions.ReadTimeout:
        return ""
    else:
        return response.text


def scrape(fetcher, pages=1):
    url = 'https://www.tecmundo.com.br/novidadess'
    items = []
    links = []
    nxSelector = ".tec--list > a.tec--btn::attr(href)"
    next_button = Selector(text=fetcher).css(nxSelector).get()
    print(url)
    print(links)
    print(next_button)
    
    for _ in range(pages):
        items.append(one_news(fetch_content()))


def list_news(fetcher):
    selected = Selector(text=fetcher)
    linkSelector = ".tec--card__title > .tec--card__title__link ::attr(href)"
    link = selected.css(linkSelector).getall()
    return(link)


def one_news(fetcher):
    selected = Selector(text=fetcher)
    titleSelector = ".tec--article__header__title::text"
    title = selected.css(titleSelector).getall()

    timeStampSelector = "div .tec--timestamp__item time::attr(datetime)"
    timeStamp = selected.css(timeStampSelector).getall()[0]

    writerSelector = "div.tec--author__info > p > a::text"
    writer = selected.css(writerSelector).getall()[0]

    scSelector = "div.tec--toolbar__item ::text"
    sc = selected.css(scSelector).getall()[0].strip().split(' ')[0]

    ccSelector = "#js-comments-btn::text"
    cc = selected.css(ccSelector).getall()[1].strip().split(' ')[0]

    summarySelector = "div.tec--article__body > p:nth-child(1)::text"
    summary = selected.css(summarySelector).get().strip()

    sourcesSelector = "div > a.tec--badge ::text"
    sources = selected.css(sourcesSelector).getall()[0].strip()

    categoriesSelector = "#js-categories > a ::text"
    categories1 = selected.css(categoriesSelector).getall()
    categories = [' '.join(src.split()) for src in categories1]
    return {
        "title": title[0],
        "timeStamp": timeStamp,
        "writer": writer,
        "sharesCount": int(sc),
        "comments_count": int(cc),
        "summary": summary,
        "sources": sources,
        "categories": categories
    }
