from tech_news.database import find_news
import csv


header_format = [
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


def csv_exporter(filepath):
    """Seu código deve vir aqui"""

    try:
        assert ".csv" in filepath
    except AssertionError:
        raise ValueError("Formato invalido")
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
    else:
        news = []
        with open(filepath, "w") as file:
            csv_writer = csv.writer(file, delimiter=";")
            # csv_writer.writerow(bla)
        # logic here: has to export + replace repetitive name
        return news

#
