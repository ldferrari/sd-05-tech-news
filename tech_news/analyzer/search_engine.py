from tech_news import database


def search_by_title(title):
    news = []
    news_by_title = database.search_news({
        "title": {
            "$regex": title,
            "$options": "i"
        }
    })

    if len(news_by_title) == 0:
        return []

    else:
        for article in news_by_title:
            news.append((article['title'], article['url']))

        return news


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
