from tech_news.database import search_news


# search_news(query): return list(db.news.find(query))
def search_by_title(title):
    # Method The title() method returns a string 
    # where the first character in every word is upper case.
    busca = search_news({"title": title.title()})
    if len(busca) == 0:
        return []
    return [(busca[0]['title'], busca[0]['url'])]


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
