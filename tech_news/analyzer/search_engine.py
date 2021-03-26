import datetime
from ..database import search_news


def search_by_key(key, query):
    result = search_news({key: query})
    return [(news["title"], news["url"]) for news in result]


def search_by_title(title):
    return search_by_key("title", title)


def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        return search_by_key("timestamp", {"regex": date})
    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
