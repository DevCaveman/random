"""
lógica para o bolao:

acertar o placar 6 pontos

acertar quem ganhou ou um empate com placar diferente 3 pontos

acertar o numero de gols de uma equipe 1 ponto


Exemplo 1
Palpite dado: - Time A 3 X 1 Time B

resultado dos jogos:

                Time A 3 X 1 Time B - 6 pontos
                Time A 3 X 0 Time B - 4 pontos (3 pelo time vencedor + 1 pelo acerto dos gols de um dos times)
                Time A 2 X 1 Time B - 4 pontos (3 pelo time vencedor + 1 pelo acerto dos gols de um dos times)
                Time A 2 X 0 Time B - 3 pontos
                Time A 0 X 1 Time B - 1 ponto
                Time A 3 X 4 Time B - 1 ponto
                Time A 0 X 0 Time B - 0 ponto


Exemplo 2
Palpite dado: - Time A 2 X 2 Time B

resultado dos jogos:

                Time A 2 X 2 Time B – 6 pontos
                Time A 1 X 1 Time B – 3 pontos
                Time A 2 X 1 Time B - 1 ponto
                Time A 1 X 2 Time B - 1 ponto
                Time A 3 X 4 Time B - 0 ponto

"""
def calcular(palpite = [1, 3], real = [2, 2]):
    '''Essa função faz o calculo e retorna os pontos'''
    
    # verifica se é exato.
    if palpite[0] == real[0] and palpite[1] == real[1]: 
        pontos = 6
    # verifica se o real é empate
    elif real[0] == real[1]: 
        # verifica se palpite é empate
        if palpite[0] == palpite[1]: 
            pontos = 3
        # verifica se acertou algum placar
        elif palpite[0] == real[0] or palpite[1] == real[1]:
            pontos = 1
        # não acertou porra nenhuma
        else:
            pontos = 0
    # verifica se acertou quem ganhou
    elif (real[0] > real[1] and palpite[0] > palpite[1]) or (real[0] < real[1] and palpite[0] < palpite[1]): 
        #verifica se acertou algum placar
        if real[0] == palpite[0] or real[1] == palpite[1]:
            pontos = 4
        else:
            pontos = 3
    # não acertou quem ganhou, mas verifacar se acertou algum placar
    elif real[0] == palpite[0] or real[1] == palpite[1]:
        pontos = 1
    # não acertou porra nenhuma
    else:
        pontos = 0

    # retorna o valor
    return pontos

def testar_calcular(exemplo1 = [3, 1], exemplo2 = [2, 2]):
    '''
        Esta função testa a função "calcular()"
        Esta função usa os valores padrões do regulamento, exemplos 1 e 2
    '''

    def get_result(exemplo):
        '''
            Chama calcular() com os valores dos exemplos automagicamente
            retornando os resultados. 
        '''
        result = [] # lista que ira conter os resultados
        if exemplo == 1:
            for i in range(0, 7):
                # valores padrão do exemplo 1
                x = (3, 3, 2, 2, 0, 3, 0)
                y = (1, 0, 1, 0, 1, 4, 0)
                result.append(calcular(exemplo1, [x[i], y[i]]))
        elif exemplo == 2:
                # valores padrão do exemplo 2
            for i in range(0, 5):
                x = (2, 1, 2, 1, 3) 
                y = (2, 1, 1, 2, 4)
                result.append(calcular(exemplo2, [x[i], y[i]]))
        # retorna uma lista com 7 indices caso exemplo 1, e 4 caso exemplo 2
        return result

    # pegando os resultados dos calculos
    valor_obtido1 = get_result(1)
    valor_obtido2 = get_result(2)
    
    # tuplas com os placares dos jogos reais, apenas para imprimir.
    valor_testado1 = ('3 x 1', '3 x 0', '2 x 1', '2 x 0', '0 x 1', '3 x 4', '0 x 0')
    valor_testado2 = ('2 x 2', '1 x 1', '2 x 1', '1 x 2', '3 x 4')

    # tuplas com as respostas esperadas(corretas) para o teste
    valor_esperado1 = (6, 4, 4, 3, 1, 1, 0)
    valor_esperado2 = (6, 3, 1, 1, 0)

    # Imprimindo os resultados
    print(' ')
    print('Executando calculos com os valores do regulamento...')
    print(' ')
    print(' > exemplo 1 - PALPITE {}'.format(exemplo1))
    for i in range(0, len(valor_esperado1)):
        if valor_obtido1[i] == valor_esperado1[i]:
            print('testando {} | obtido {} | esperado {} -> OK'.format(valor_testado1[i], valor_obtido1[i], valor_esperado1[i]))
        else:
            print('testando {} | obtido {} | esperado {} -> falha'.format(valor_testado1[i], valor_obtido1[i], valor_esperado1[i]))
    print(' ')
    print(' > exemplo 2 - PALPITE {}'.format(exemplo2))
    for i in range(0, len(valor_esperado2)):
        if valor_obtido2[i] == valor_esperado2[i]:
            print('testando {} | obtido {} | esperado {} -> OK'.format(valor_testado2[i], valor_obtido2[i], valor_esperado2[i]))
        else:
            print('testando {} | obtido {} | esperado {} -> falha'.format(valor_testado2[i], valor_obtido2[i], valor_esperado2[i]))
