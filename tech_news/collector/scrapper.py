import requests
from time import sleep
from parsel import Selector


search = ['div.tec--toolbar__item::text', 'button#js-comments-btn::text']


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


def scrape(fetcher, pages=1):
    page = Selector(text=fetcher)
    url = page.css('head link::attr(href)')[20].get()
    title = page.css('h1.tec--article__header__title::text').get().strip()
    timestamp = page.css('time::attr(datetime)').get()
    writer = page.css('a.tec--author__info__link::text').get().strip()
    shares_count = page.css(search[0])[1].get()
    shares_count.replace('Compartilharam', '').strip()
    comments_count = page.css(search[1])[1].get()
    comments_count.replace('Comentários', '').strip()
    summary = page.css('div.tec--article__body p').get()
    sources = page.css('div.z--mb-16.z--px-16 a.tec--badge::text').getall()
    for source in sources:
        sources[sources.index(source)] = source.strip()
    categories = page.css('div#js-categories a::text').getall()
    for categ in categories:
        categories[categories.index(categ)] = categ.strip()
    return [{
        'url': url,
        'title': title,
        'timestamp': timestamp,
        'writer': writer,
        'shares_count': shares_count,
        'comments_count': comments_count,
        'summary': summary,
        'sources': sources,
        'categories': categories,
        }]
