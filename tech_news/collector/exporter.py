import csv
# from pymongo import MongoClient
from database import find_news


def csv_exporter(filepath):
    # DB_HOST = config("DB_HOST", default="localhost")
    # DB_PORT = config("DB_PORT", default="27017")
    # with client = MongoClient(host=DB_HOST, port=int(DB_PORT))
    #    db = client.tech_news
    try:
        assert filepath.endswith('.csv')
    except AssertionError:
        raise ValueError("Formato invalido")
    else:
        with open(filepath, "w") as file:
            writer = csv.writer(file, delimiter=";")
            headers = [
                "url",
                "title",
                "timestamp",
                "writer",
                "shares_count",
                "comments_count",
                "summary",
                "sources",
                "categories",
            ]
            writer.writerow(headers)
            news = find_news()
            writer.writerow(news)
