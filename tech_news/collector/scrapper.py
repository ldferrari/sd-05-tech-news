import requests
from time import sleep
from parsel import Selector


search = {
    'url_list': 'h3 a.tec--card__title__link::attr(href)',
    'title': '#js-article-title::text',
    'timestamp': 'time::attr(datetime)',
    'writer': '.tec--author__info__link::text',
    'shares': 'div.tec--toolbar__item::text',
    'comments': 'button#js-comments-btn::attr(data-count)',
    'summary': '.tec--article__body > p:nth-child(1)::text',
    'sources': 'a.tec--badge::text'
}


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
    except requests.Timeout:
        return ''
    else:
        if (response.status_code != 200):
            return ''
        sleep(delay)
        return response.text


def parsed_news(notice, url):
    text = Selector(notice)
    url = url
    title = text.css(search['title']).get()
    timestamp = text.css(search['timestamp']).get()
    writer = text.css(search['writer']).get()
    shares_count = text.css(search['shares']).get().strip()[:1]
    comments_count = text.css(search['comments']).get()
    summary = text.css(search['summary']).get()
    sources = text.css(search['sources']).getall()
    for source in sources:
        sources[sources.index(source)] = source.strip()
    categories = text.css('div#js-categories a::text').getall()
    for categ in categories:
        categories[categories.index(categ)] = categ.strip()
    return {
        'url': url,
        'title': title,
        'timestamp': timestamp,
        'writer': writer,
        'shares_count': shares_count,
        'comments_count': comments_count,
        'summary': summary,
        'sources': sources,
        'categories': categories,
    }


def scrape(fetcher, pages=1):
    main_page = "https://www.tecmundo.com.br/novidades"
    news = []
    for page in range(pages):
        news_list = Selector(text=fetcher(main_page))
        urls = news_list.css(search['url_list']).getall()
        for url in urls:
            news.append(parsed_news(fetcher(url), url=url))
        return news
