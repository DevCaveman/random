#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('Classes')

from arquivo import Arquivo

conta = Arquivo.make_contas()
dicionario = { 'penis': 'pequeno' }
conta.adicionar(dicionario)
conta.ler()
dicionario = { 'teta': 'seca' }
conta.adicionar(dicionario)
conta.ler()
