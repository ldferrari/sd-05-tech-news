import csv

def csv_importer(filepath):
    """Importa um arquivo CSV e retorna os dados como objeto."""

    ext = filepath[-3:]
    valid_header = [
        'url',
        'title',
        'timestamp',
        'writer',
        'shares_count',
        'comments_count',
        'summary',
        'sources',
        'categories'
    ]

    if (ext != 'csv'):
        raise ValueError('Formato invalido')

    try:
        with open(filepath) as file:
            csv_reader = csv.reader(file, delimiter=";")
            header, *data = csv_reader
            print(data)

            if header != valid_header:
                raise ValueError('Cabeçalhos não compativeis')

            data_result = [
                {header[i]: content[i] for i in range(len(content))}
                for content in data
            ]

            return data_result

    except FileNotFoundError:
        raise ValueError(f'Arquivo {filepath} não encontrado')
