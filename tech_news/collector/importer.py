import csv


def csv_importer(filepath):
    if filepath.split('.')[1] == 'csv':
        with open(filepath, 'r') as news:
            ler = csv.reader(news, delimiter=';')
            print(ler)


csv_importer('file_csv.csv')
