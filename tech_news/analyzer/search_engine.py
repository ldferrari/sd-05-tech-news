from tech_news.model import tech_news_model

cursor = tech_news_model.find_cursor


def search_by_title(title):
    """Seu código deve vir aqui"""
    PARAMS = {"title": {"$regex": f".*{title}.*", "$options": "i"}}
    PROJECTION = {"_id": 0, "title": 1, "url": 1}
    search = cursor(params=PARAMS, projection=PROJECTION)
    if len(search) == 0:
        return []
    result = [tuple(reversed(item.values())) for item in search]
    print(result)
    return result


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
