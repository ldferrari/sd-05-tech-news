from tech_news import database


def search_by_title(title):
    """Seu código deve vir aqui"""
    title_news = database.search_news(
        {"title": {"$regex": title, "$options": "i"}}
    )
    filtered_news = []
    for news in title_news:
        filtered_news.append((news['title'], news['url']))
    return filtered_news


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
