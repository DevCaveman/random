"""
    Classe responsável pela escrita e leitura do Arquivo Json
que contém os dados das contas.
"""
import json

class Arquivo:

    def __init__(self, nome_arquivo : str):
        self.__nome_arquivo = nome_arquivo + '.json'
        
    def ler(self):
        try:
            with open(self.__nome_arquivo, 'r') as arquivo_contas:
                return json.load(arquivo_contas)
        except Exception as err:
            print('Erro -> {}'.format(err))

    def escrever(self, data_to_write : dict):
        try:
            with open(self.__nome_arquivo, 'w') as arquivo_contas:
                json.dump(data_to_write, arquivo_contas)
        except Exception as err:
            print('Erro -> {}'.format(err))
