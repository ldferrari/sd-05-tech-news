from tech_news.database import search_news


def search_by_title(title):
    """Seu código deve vir aqui"""
    title = {"title": title.title()}
    search = search_news(title)
    if search == []:
        return []
    news = [(search[0]["title"], search[0]["url"])]
    return news


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
