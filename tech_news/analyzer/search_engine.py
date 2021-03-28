from tech_news import database
import datetime


def search_by_title(title):
    # https://docs.mongodb.com/manual/reference/operator/query/regex/
    news_by_title = database.search_news(
        {"title": {"$regex": title, "$options": "i"}}
    )
    return [(news["title"], news["url"]) for news in news_by_title]


def search_by_date(date):
    try:
        # https://www.codevscolor.com/date-valid-check-python
        year, month, day = date.split('-')
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        raise ValueError("Data inválida")
    else:
        news_by_date = database.search_news({"timestamp": {"$regex": date}})
        return([(news["title"], news["url"]) for news in news_by_date])


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""


if __name__ == "__main__":
    search_by_date("2020-11-23")
