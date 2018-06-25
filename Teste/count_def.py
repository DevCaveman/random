'''
    Função que tem um atributo que conta quantas vezes é executado
'''
def imprime():
    # atributo contador
    imprime.count += 1

    # retorno baseado no número de vezes
    if imprime.count == 1:
        return 'um'
    elif imprime.count == 2:
        return 'dois'
    elif imprime.count == 3:
        imprime.count = 0
        return 'três'

# iniciando o contador com 0
imprime.count = 0

# imprimindo
for i in range(1, 5):
    print(imprime()) # vai retornar um
    print(imprime()) # vai retornar dois
    print(imprime()) # vai retornar tres

