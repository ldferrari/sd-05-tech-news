from tech_news import database


def search_by_title(title):
    search_news = database.search_news(
        {
            "title":
                {
                    "$regex": title, "$options": "i"
                }
        }
    )

    if len(search_news) == 0:
        return []

    return [(search_news[0]["title"], search_news[0]["url"])]


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
