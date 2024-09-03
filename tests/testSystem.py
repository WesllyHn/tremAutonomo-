# tests/test_sistema.py

import unittest
from system import Sistema

class TestSistema(unittest.TestCase):

    def test_execucao_comandos_validos(self):
        sistema = Sistema()
        posicao_final = sistema.executar_comandos(["DIREITA", "ESQUERDA"])
        self.assertEqual(posicao_final, 0)

    def test_execucao_comando_invalido(self):
        sistema = Sistema()
        posicao_final = sistema.executar_comandos(["DIREITA", "INDEFINIDO"])
        self.assertIsNone(posicao_final)
