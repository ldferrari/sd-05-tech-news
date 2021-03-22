from sys import exit
from tech_news.collector import exporter, importer, scrapper


def execute_option(answer):
    option = ""
    if answer == "1":
        print("Digite o nome do arquivo CSV a ser importado:")
        option = input()
        importer.csv_importer(option)
    elif answer == "2":
        print("Digite o nome do arquivo CSV a ser exportado:")
        option = input()
        exporter.csv_exporter(option)
    elif answer == "3":
        print("Digite a quantidade de páginas a serem raspadas:")
        option = input()
        scrapper.scrape(option)
    

def collector_menu():
    """Seu código deve vir aqui"""
    print("Selecione uma das opções a seguir:")
    print(" 1 - Importar notícias a partir de um arquivo CSV;")
    print(" 2 - Exportar notícias para CSV;")
    print(" 3 - Raspar notícias online;")
    print(" 4 - Sair.")
    try:
        answer = input()
        assert answer in ["1", "2", "3", "4"]
    except AssertionError:
        print("Opção inválida\n")
        raise AssertionError("Opção inválida")
    else:
        if answer == "4":
            print("Encerrando script")
        else:
            execute_option(answer)


def analyzer_menu():
    """Seu código deve vir aqui"""
