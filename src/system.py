# src/sistema.py

from train import TremAutonomo

class Sistema:
    def __init__(self):
        self.trem = TremAutonomo()

    def executar_comandos(self, comandos):
        try:
            posicao_final = self.trem.mover(comandos)
            print(f"Posição Final do Trem: {posicao_final}")
            return posicao_final
        except ValueError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Erro crítico: {e}")

if __name__ == "__main__":
    sistema = Sistema()
    
    # Exemplo de uso
    comandos = ["DIREITA", "DIREITA", "ESQUERDA"]
    sistema.executar_comandos(comandos)
