# src/comando.py

from enum import Enum

class Comando(Enum):
    ESQUERDA = "ESQUERDA"
    DIREITA = "DIREITA"

    @staticmethod
    def from_str(label):
        if label.upper() in Comando.__members__:
            return Comando[label.upper()]
        else:
            raise ValueError(f"Comando inválido: {label}")
