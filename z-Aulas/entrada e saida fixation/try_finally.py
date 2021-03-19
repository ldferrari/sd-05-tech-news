try:
    arquivo = open('arquivs.txt', 'r')
except OSError:
    print('arquivo inexistente')
else:
    print('arquivo manipulado e fechado com sucesso')
finally: 
    print('tentativa de abrir o arquivo')