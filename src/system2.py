class TremAutonomo:
    def __init__(self):
        self.posicao = 2
        self.movimentos_consecutivos = 5
        self.direcao_anterior = None

    def mover(self, comandos):
        if not comandos:
            raise ValueError("A lista de comandos não pode estar vazia.")
        
        posicao_final = self.posicao
        for comando in comandos:
            if comando not in ["ESQUERDA", "DIREITA"]:
                raise ValueError(f"Comando desconhecido: {comando}")
            
            if self.movimentos_consecutivos >= 20 and comando == self.direcao_anterior:
                raise ValueError("Mais de 20 movimentos consecutivos na mesma direção.")
            
            if abs(posicao_final) >= 50:
                print("O trem atingiu o limite de 50 posições.")
                break

            if comando == "ESQUERDA":
                posicao_final -= 1
            elif comando == "DIREITA":
                posicao_final += 1
            
            self.movimentos_consecutivos = self.movimentos_consecutivos + 1 if comando == self.direcao_anterior else 1
            self.direcao_anterior = comando

        self.posicao = posicao_final
        return posicao_final

# Exemplo de execução
if __name__ == "__main__":
    trem = TremAutonomo()

    comandos = ["DIREITA", "DIREITA", "ESQUERDA", "DIREITA", "DIREITA", "DIREITA", "DIREITA", "ESQUERDA"]
    
    try:
        posicao_final = trem.mover(comandos)
        print(f"Posição final do trem: {posicao_final}")
    except ValueError as e:
        print(f"Erro: {e}")
