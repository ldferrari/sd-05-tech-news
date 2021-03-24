# https://docs.mongodb.com/manual/reference/operator/query/regex/
# https://www.programiz.com/python-programming/datetime/strptime
from tech_news import database
from datetime import datetime


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
    try:
        datetime.strptime(date, "%Y-%m-%d")

        data = database.search_news({'timestamp': {'$regex': date}})
    except ValueError:
        raise ValueError('Data inválida')
    else:
        if len(data) == 0:
            return data

        news = []
        c = 0
        while c < len(data):
            news.append((news[c]['title'], news[c]['url']))
        return news


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
