# Referência: https://stackoverflow.com/questions/10610131/
# checking-if-a-field-contains-a-string

from tech_news import database


def search_by_title(title):
    """Seu código deve vir aqui"""

    news = database.search_news({"title": {"$regex": title, "$options": "i"}})
    print(news)
    return [(item["title"], item["url"]) for item in news]


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""


if __name__ == "__main__":
    search_by_title("VAMOSCOMTUDO")
