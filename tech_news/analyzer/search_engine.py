import datetime
from tech_news.database import search_news
# from pymongo import MongoClient
# from decouple import config

# DB_HOST = config("DB_HOST", default="localhost")
# DB_PORT = config("DB_PORT", default="27017")

# client = MongoClient(host=DB_HOST, port=int(DB_PORT))
# db = client.tech_news


def search_by_title(title):
    insensitive_title = {"title": {"$regex": title, "$options": "i"}}
    # news = list(db.news.find(insensitive_title))
    news = search_news(insensitive_title)
    resultado = []
    for noticia in news:
        resultado.append((noticia['title'], noticia['url']))
    return resultado


def search_by_date(date):
    try:
        format = "%Y-%m-d"
        datetime.datetime.strptime(date, format)
    except AssertionError:
        raise ValueError("Data inválida")
    else:
        news = search_news(date)
        resultado = []
        for noticia in news:
            resultado.append((noticia['title'], noticia['url']))
        return resultado


def search_by_source(source):
    insensitive_source = {"source": {"$regex": source, "$options": "i"}}
    # news = list(db.news.find(insensitiveTitle))
    news = search_news(insensitive_source)
    resultado = []
    for noticia in news:
        resultado.append((noticia['title'], noticia['url']))
    return resultado


def search_by_category(category):
    insensitive_category = {"category": {"$regex": category, "$options": "i"}}
    # news = list(db.news.find(insensitiveTitle))
    news = search_news(insensitive_category)
    resultado = []
    for noticia in news:
        resultado.append((noticia['title'], noticia['url']))
    return resultado
