import sys
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
# from tech_news.analyzer.ratings import top_5_news, top_5_categories

from tech_news.database import create_news


def execute_option(answer):
    option = ""
    if answer == "1":
        option = input("Digite o nome do arquivo CSV a ser importado:")
        data = csv_importer(option)
        create_news(data)
    elif answer == "2":
        print("Digite o nome do arquivo CSV a ser exportado:")
        option = input()
        csv_exporter(option)
    elif answer == "3":
        option = input("Digite a quantidade de páginas a serem raspadas:")
        data = scrape(fetcher=fetch_content, pages=option)


def collector_menu():
    """Seu código deve vir aqui"""
    answer = input(
        "Selecione uma das opções a seguir:\n"
        " 1 - Importar notícias a partir de um arquivo CSV;\n"
        " 2 - Exportar notícias para CSV;\n"
        " 3 - Raspar notícias online;\n"
        " 4 - Sair.\n"
    )
    result = "Opção inválida"
    if answer not in ["1", "2", "3", "4"]:
        print(result, file=sys.stderr)
    if answer == "4":
        print("Encerrando script")
    execute_option(answer)


def analyzer_menu():
    """Seu código deve vir aqui"""
