# https://docs.mongodb.com/manual/reference/operator/query/regex/
from tech_news import database


def search_by_title(title):
    data = database.search_news({'title': {'$regex': title, '$options': 'i'}})
    if len(data) == 0:
        return data

    news = []
    c = 0
    while c < len(data):
        news.append((data[c]['title'], data[c]['url']))
        c += 1

    return news


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
