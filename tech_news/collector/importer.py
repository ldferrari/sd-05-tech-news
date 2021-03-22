import csv


def csv_importer(filepath):
    try:
        assert filepath.endswith('.csv')
        with open(filepath) as file:
            arquivo = csv.reader(file, delimiter=';', quotechar='"')
            header, *data = arquivo
    except FileNotFoundError:
        raise ValueError(f'Arquivo {filepath} não encontrado')
    except AssertionError:
        raise ValueError("Formato invalido")
    except OSError:
        raise ValueError("Formato invalido")
    else:
        dicionario = {}
        acc = 0
        for item in header:
            dicionario[item] = data[item]
        #    acc += 1
        # if header != 'url;title;timestamp;writer;shares_count;comments_count;
        # summary;sources;categories':
        #    raise Exception("Cabeçalho errado")
        return dicionario
