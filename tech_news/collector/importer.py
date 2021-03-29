import csv


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    data = []
    try:
        with open(filepath) as file:
            read_file = csv.DictReader(file, delimiter=";")
            for item in read_file:
                data.append(item)
            return data

    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")