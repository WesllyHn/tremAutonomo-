# tests/test_comando.py

import unittest
from command import Comando

class TestComando(unittest.TestCase):

    def test_comando_valido(self):
        self.assertEqual(Comando.from_str("ESQUERDA"), Comando.ESQUERDA)
        self.assertEqual(Comando.from_str("DIREITA"), Comando.DIREITA)

    def test_comando_invalido(self):
        with self.assertRaises(ValueError):
            Comando.from_str("INDEFINIDO")
