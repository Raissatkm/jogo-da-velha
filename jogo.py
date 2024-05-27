class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [' ' for _ in range(9)]
        self.jogador_atual = 'X'

    def exibir_tabuleiro(self):
        for i in range(3):
            print(f"{self.tabuleiro[3 * i]} | {self.tabuleiro[3 * i + 1]} | {self.tabuleiro[3 * i + 2]}")
            if i < 2:
                print("--+---+--")
                

    def jogar(self):
        self.exibir_tabuleiro()  
        while True:
            print(f"Jogador {self.jogador_atual}, escolha uma posição (0-8): ", end=" ")
            try:
                posicao = int(input().strip())  
                if posicao < 0 or posicao > 8 or self.tabuleiro[posicao] != ' ':
                    print("Posição inválida. Tente novamente.")
                    continue
                

                self.tabuleiro[posicao] = self.jogador_atual
                self.exibir_tabuleiro()  
                if self.checar_vencedor():
                    print(f"Parabéns! Jogador {self.jogador_atual} venceu!")
                    break
                

                if ' ' not in self.tabuleiro:
                    print("Empate! O tabuleiro está cheio.")
                    break

                self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")


    def checar_vencedor(self):
        combinacoes_vencedoras = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  
            (0, 4, 8), (2, 4, 6)  
        ]
        for a, b, c in combinacoes_vencedoras:
            if self.tabuleiro[a] == self.tabuleiro[b] == self.tabuleiro[c] != ' ':
                return True
        return False


jogo1 = JogoDaVelha()
jogo1.jogar()
