from command import Comando
from restriction import Restricoes

class TremAutonomo:
    def __init__(self):
        self.posicao_atual = 5
        self.movimentos_totais = 18
        self.movimentos_direcao_atual = 12
        self.direcao_atual = None

    def mover(self, comandos):
        for comando in comandos:
            # Valida o comando
            comando = Comando.from_str(comando)

            # Verifica se atingiu o limite de movimentos
            Restricoes.verificar_limites(self.movimentos_totais, self.movimentos_direcao_atual if self.direcao_atual == comando else 1)

            # Atualiza a direção e os contadores
            if self.direcao_atual == comando:
                self.movimentos_direcao_atual += 1
            else:
                self.direcao_atual = comando
                self.movimentos_direcao_atual = 1

            # Realiza o movimento
            if comando == Comando.DIREITA:
                self.posicao_atual += 1
            elif comando == Comando.ESQUERDA:
                self.posicao_atual -= 1

            # Incrementa o total de movimentos
            self.movimentos_totais += 1

        return self.posicao_atual
