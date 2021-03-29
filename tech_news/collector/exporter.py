from tech_news import database
import csv


def csv_exporter(filepath):

    valid_header = [
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

    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    with open(filepath, "w") as file:
        csv_writer = csv.DictWriter(
            file, fieldnames=valid_header, delimiter=";"
        )

        news_db = database.find_news()
        for linha in news_db:
            for chave in linha:
                if type(linha[chave]) == list:
                    linha[chave] = ",".join(linha[chave])

        csv_writer.writeheader()
        csv_writer.writerows(news_db)
