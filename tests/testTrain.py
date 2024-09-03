# tests/test_trem_autonomo.py

import unittest
from train import TremAutonomo
from command import Comando

class TestTremAutonomo(unittest.TestCase):

    def test_movimento_simples(self):
        trem = TremAutonomo()
        self.assertEqual(trem.mover([Comando.DIREITA.value]), 1)
        self.assertEqual(trem.mover([Comando.ESQUERDA.value]), 0)

    def test_movimento_consecutivo(self):
        trem = TremAutonomo()
        trem.mover([Comando.DIREITA.value] * 20)
        with self.assertRaises(Exception):
            trem.mover([Comando.DIREITA.value])

    def test_limite_movimentos(self):
        trem = TremAutonomo()
        trem.mover([Comando.DIREITA.value] * 50)
        with self.assertRaises(Exception):
            trem.mover([Comando.DIREITA.value])
