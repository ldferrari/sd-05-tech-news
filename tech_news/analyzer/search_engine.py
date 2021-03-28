from tech_news import database
from datetime import datetime


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
            # parênteses a mais porque o retorno precisa ser uma tupla

        return news


def search_by_date(date):
    news = []

    try:
        datetime.strptime(date, "%Y-%m-%d")

        news_by_date = database.search_news({
            "timestamp": {
                "$regex": date
            }
        })

        if len(news_by_date) == 0:
            return []

        else:
            for article in news_by_date:
                news.append((article['title'], article['url']))
                # parênteses a mais porque o retorno precisa ser uma tupla

            return news

    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    news = []
    news_by_source = database.search_news({
        "sources": {
            "$regex": source,
            "$options": "i"
        }
    })

    if len(news_by_source) == 0:
        return []

    else:
        for article in news_by_source:
            news.append((article['title'], article['url']))
            # parênteses a mais porque o retorno precisa ser uma tupla

        return news


def search_by_category(category):
    """Seu código deve vir aqui"""

# $regex operator
# https://docs.mongodb.com/manual/reference/operator/query/regex/
# método datetime.strptime
# https://docs.python.org/3/library/datetime.html
