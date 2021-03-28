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

    news = database.find_news()

    try:
        assert filepath.endswith(".csv")

        with open(filepath, "w") as file:
            csv_writer = csv.DictWriter(
                file, fieldnames=valid_header, delimiter=";"
            )

            for rows in news:
                for key in rows:
                    # print(key, '--------- chaves')
                    if type(rows[key]) == list:
                        # print(rows[key], '--- antes')
                        rows[key] = ",".join(rows[key])
                        # print(rows[key], '--- depois')

                csv_writer.writeheader()
                csv_writer.writerows(news)
                # print(news)

    # mesmo except para os 2 assertion errors (.csv & header)
    except AssertionError:
        raise ValueError("Formato invalido")

    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
