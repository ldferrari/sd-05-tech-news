from tech_news.database import search_news


def search_by_title(title):
    """Retorna o titulo e url das noticias encontradas."""

    news = []
    news_by_title = search_news({
        'title': {
            '$regex': title,
            '$options': 'i'
        }
    })

    for new in news_by_title:
        news.append((new['title'], new['url']))

    return news

def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
