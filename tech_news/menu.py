import sys
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.database import create_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
)


def collector_menu():
    INPUT = input(
        "Selecione uma das opções a seguir:\n"
        " 1 - Importar notícias a partir de um arquivo CSV;\n"
        " 2 - Exportar notícias para CSV;\n"
        " 3 - Raspar notícias online;\n"
        " 4 - Sair.\n"
    )

    if INPUT == "1":
        PATH = input("Digite o nome do arquivo CSV a ser importado:")
        CONTENT = csv_importer(PATH)
        create_news(CONTENT)
    elif INPUT == "2":
        PATH = input("Digite o nome do arquivo CSV a ser exportado:")
        csv_exporter(PATH)
    elif INPUT == "3":
        PAGE_QNT = input("Digite a quantidade de páginas a serem raspadas:")
        DATA = scrape(fetcher=fetch_content, pages=int(PAGE_QNT))
        create_news(DATA)
    elif INPUT == "4":
        print("Encerrando script")
    else:
        print("Opção inválida", file=sys.stderr)


def analyzer_menu():
    INPUT = input(
        "Selecione uma das opções a seguir:\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por fonte;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.\n"
    )

    if INPUT == "1":
        TITLE = input("Digite o título: ")
        search_by_title(TITLE)
    elif INPUT == "2":
        DATE = input("Digite a data no formato aaaa-mm-dd: ")
        search_by_date(DATE)
    elif INPUT == "3":
        SOURCE = input("Digite a fonte: ")
        search_by_source(SOURCE)
    elif INPUT == "7":
        return print("Encerrando script")
    else:
        return print("Opção inválida", file=sys.stderr)
