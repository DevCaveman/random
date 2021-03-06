#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

class Arquivo:

    def __init__(self, nome_arquivo : str):
        self._nome_arquivo = nome_arquivo + '.json'
        
    def __repr__(self):
        return f'Arquivo({self._nome_arquivo})'

    def ler(self):
        try:
            with open(self._nome_arquivo, 'r') as arquivo_contas:
                return json.load(arquivo_contas)
        except Exception as err:
            print('Erro -> {}'.format(err))
            print('Creating json file -> {}'.format(self._nome_arquivo))
            self.escrever({})

    def escrever(self, data_to_write : dict):
        try:
            with open(self._nome_arquivo, 'w') as arquivo_contas:
                json.dump(data_to_write, arquivo_contas)
        except Exception as err:
            print('Erro -> {}'.format(err))

    def adicionar(self, data_to_add : dict):
        data = self.ler()
        data.update(data_to_add)
        self.escrever(data)

    @classmethod
    def make_contas(cls):
        _obj = cls('contas')
        _obj.ler()
        return _obj
