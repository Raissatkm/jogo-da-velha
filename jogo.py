class JogodaVelha():
    def __init__(self):
        self.tabuleiro = [" " for _ in range(9)]
        self.jogador_atual = "X"
    
    
    def mostrar_tabuleiro(self):
        for i in range(3):
            print(f"{self.tabuleiro[3*i]} | {self.tabuleiro[3*i+ 1]} | {self.tabuleiro[3*i +2]}")
            if i < 2:
                print("--+---+--")