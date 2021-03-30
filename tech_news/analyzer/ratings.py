import pymongo
from tech_news.database import db


def top_5_news():
    """Seu código deve vir aqui"""
    top_5_news = []
    news = (db.news.find({}).sort([
        ('shares_count', pymongo.DESCENDING),
        ('comments_count', pymongo.DESCENDING),
        ('title', pymongo.ASCENDING)
    ]).limit(5))

    for new in news:
        top_5_news.append((new['title'], new['url']))

    return top_5_news


def top_5_categories():
    """Seu código deve vir aqui"""
