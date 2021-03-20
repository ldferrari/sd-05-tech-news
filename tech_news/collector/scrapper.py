import requests
from parsel import Selector
from time import sleep
from enum import Enum
from sys import argv


Classes = {
    "card": ".tec--card",
    "link": "div.tec--list__item > article > div > h3 > a::attr(href)",
    "title": ".tec--card__title", 
    "shares_count": "div.tec--toolbar__item:nth-child(1)::text",
    "comments": "#js-comments-btn::attr(data-count)",
    "sources": ".z--mb-16 > div > a::text",
    "categories": "div.z--w-1-3 > ul > li > a::text",
    "summary": ".tec--article__body > p:nth-child(1)::text"
}


def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=timeout)
    except requests.RequestException:
        print("deu ruim mano")
        return ""
    else:
        if response.status_code != 200:
            return ''
        sleep(delay)
        return response.text


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
    url = "http://techmundo.com.br/novidades"
    if __name__ == '__main__':
        url = "http://127.0.0.1:5500/tests/test_collector/index.html"
    url2 = "http://127.0.0.1:5500/tests/test_collector/notice.html"
    all_news = []
    news_links = []
    parsed_news = []
    for _ in range(pages):
        news = []
        selector = Selector(text=fetcher(url)) 
        news_links.extend(selector.css(Classes["link"]).getall())
    if __name__ == '__main__':
        news_links = [url2]
    for link in news_links:
        all_news.append({"url": link, 'response': fetcher(link)})
    for news in all_news:
        parsed_news.append(parse_news(news))
    print(">>>>>>: ", len(news_links), '\n', news_links)
    return parsed_news


def parse_news(news):
    parsed_news = {
    "url": news['url']        
    }
    selector = Selector(text=news['response'])
    parsed_news["title"] = selector.css('#js-article-title::text').get().strip()
    parsed_news["timestamp"] = selector.css('#js-article-date::attr(datetime)').get().strip()
    parsed_news["writer"] = selector.css('.tec--author__info__link::text').get().strip()
    shares_count = selector.css(Classes['shares_count']).get().strip()
    shares_count = int(shares_count.split()[0])
    parsed_news['shares_count'] = shares_count
    summary = selector.css(Classes["summary"]).get().strip()
    parsed_news["summary"] = summary
    comments = selector.css(Classes['comments']).get()
    comments = int(comments)
    parsed_news["comments_count"] = comments
    sources = selector.css(Classes['sources']).getall()
    parsed_news["sources"] = [src.strip() for src in sources]
    categories = selector.css(Classes["categories"]).getall()
    parsed_news["categories"] = [cat.strip() for cat in categories]
    return parsed_news


if __name__ == '__main__':
    url = "https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm"
    # if argv[1] or argv[1] != '':
    #     url = argv[1]
    result = scrape(fetcher=fetch_content)
    print(result)
