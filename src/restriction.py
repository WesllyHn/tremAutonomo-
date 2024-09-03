# src/restricoes.py

class Restricoes:
    MOVIMENTOS_MAXIMOS = 50
    MOVIMENTOS_CONSECUTIVOS_MAXIMOS = 20

    @staticmethod
    def verificar_limites(movimentos_totais, movimentos_direcao_atual):
        if movimentos_totais >= Restricoes.MOVIMENTOS_MAXIMOS:
            raise Exception("O trem atingiu o limite de movimentos permitidos.")

        if movimentos_direcao_atual > Restricoes.MOVIMENTOS_CONSECUTIVOS_MAXIMOS:
            raise Exception("O trem atingiu o limite de movimentos consecutivos na mesma direção.")
