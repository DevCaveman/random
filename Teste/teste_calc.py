# Importando o as funções que iremos testar.
# E o framework unittest para realizar os testes nas funções.
from calculadora import soma, subtrai, multiplica, divide
from unittest import TestCase, main

# Testes
class TesteCalculadora(TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 2), 4)

    def test_subtrai(self):
        self.assertEqual(subtrai(2, 2), 0)

    def test_multiplica(self):
        self.assertEqual(multiplica(2, 2), 4)

    def test_divide(self):
        self.assertEqual(divide(2, 2), 1)

if __name__ == '__main__':
    main()
