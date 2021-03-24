import csv


def csv_importer(filepath):
    if filepath.split('.')[1] != "csv":
        raise ValueError("Formato invalido")
    try:
        with open(filepath) as file:
            reader_file = csv.DictReader(file, delimiter=";")
            for linha in reader_file:
                return [linha]
    except FileNotFoundError:
        raise ValueError(f'Arquivo {filepath} não encontrado')
