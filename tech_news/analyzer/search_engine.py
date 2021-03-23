from tech_news import database


def search_by_title(title):
    """Seu código deve vir aqui"""
    # 1/ Use search_news functions from database.py, writing pymongo query
    # & selecting by title & providing case insensitive (option i)
    NEWS = database.search_news(
        {"title": {"$regex": title, "$options": "i"}}
    )
    # print(NEWS)
    # 2/ Caso nenhuma notícia seja encontrada, retornar lista vazia
    if len(NEWS) == 0:
        return []
    # 3/ Formatar resposta pedida - lista de tuplas [("title", "url")]
    return [(NEWS[0]["title"], NEWS[0]["url"])]


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""


# https://kb.objectrocket.com/mongo-db/how-to-query-mongodb-documents-with-regex-in-python-362
