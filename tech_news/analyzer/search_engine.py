from tech_news import database
import datetime


REGEX = "$regex"


def search_by_title(title):
    news = database.search_news({"title": {REGEX: title, "$options": "-i"}})
    if len(news) == 0:
        return news

    return [(news[0]["title"], news[0]["url"])]


def search_by_date(date):
    try:
        new_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        print(new_date)
        news = database.search_news({"timestamp": {REGEX: date}})
    except ValueError:
        raise ValueError("Data inválida")
    else:
        if len(news) == 0:
            return news
        return [(news[0]["title"], news[0]["url"])]


def search_by_source(source):
    news = database.search_news({"sources": {REGEX: source, "$options": "-i"}})

    if len(news) == 0:
        return news

    return [(news[0]["title"], news[0]["url"])]


def search_by_category(category):
    """Seu código deve vir aqui"""
