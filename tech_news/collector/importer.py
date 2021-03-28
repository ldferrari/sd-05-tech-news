import csv


def csv_importer(filepath):
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

    try:
        assert filepath.endswith(".csv")

        with open(filepath) as file:
            csv_reader = csv.reader(file, delimiter=";")
            # separa o header do restante (referência: conteúdo)
            header, *data = csv_reader

            assert header == valid_header

            result = [
                {header[i]: content[i] for i in range(len(content))}
                for content in data
            ]

            return result

    # mesmo except para os 2 assertion errors (.csv & header)
    except AssertionError:
        raise ValueError("Formato invalido")

    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")

# https://docs.python.org/3/library/exceptions.html#ValueError
