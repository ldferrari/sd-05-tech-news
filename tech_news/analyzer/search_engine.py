from tech_news import database


def search_by_title(title):
    busca = database.search_news(
        {"title": {"$regex": title, "$options": "-i"}}
    )
    if len(busca) == 0:
        return []

    news = []
    for new in busca:
        news.append((new["title"], new["url"]))
    return news


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
