# tests/test_restricoes.py

import unittest
from restriction import Restricoes

class TestRestricoes(unittest.TestCase):

    def test_limite_movimentos_totais(self):
        with self.assertRaises(Exception):
            Restricoes.verificar_limites(50, 10)

    def test_limite_movimentos_consecutivos(self):
        with self.assertRaises(Exception):
            Restricoes.verificar_limites(10, 21)
