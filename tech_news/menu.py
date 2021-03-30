import sys
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.database import create_news


def collector_menu():
    mensagem = ('''
Selecione uma das opções a seguir:

1 - Importar notícias a partir de um arquivo CSV;
2 - Exportar notícias para CSV;
3 - Raspar notícias online;
4 - Sair''')

    option = int(input(mensagem))

    if option == 1:
        pathfile = input("Digite o nome do arquivo CSV a ser importado:")
        dados = csv_importer(pathfile)
        create_news(dados)
    elif option == 2:
        pathfile = input("Digite o nome do arquivo CSV a ser exportado:")
        csv_exporter(pathfile)
    elif option == 3:
        quantidade = int(
            input("Digite a quantidade de páginas a serem raspadas:"))
        dados = scrape(fetcher=fetch_content, pages=quantidade)
        create_news(dados)
    elif option == 4:
        print("Encerrando script")
    else:
        sys.stderr.write("Opção inválida\n")


def analyzer_menu():
    """Seu código deve vir aqui"""

#   https://codesource.io/ways-to-implement-python-switch-case-statement/
