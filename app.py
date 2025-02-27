import random

class JogoNim():
    def __init__(self, num_pedras, max_retirada, tipo_jogo):
        self.num_pedras = num_pedras
        self.max_retirada = max_retirada
        self.tipo_jogo = tipo_jogo
        self.turno = 0

    def exibir_status(self):
        print(f"Numeros de pedras restantes: {self.num_pedras}")
        if self.turno == 0:
            print("VEZ DO JOGADOR 1!")
        else:
            print("VEZ DO JOGADOR 2!")

    def jogada_jogador(self, pedras_retirada):
        if 1 <= pedras_retirada <= self.max_retirada and pedras_retirada <= self.num_pedras:
            self.num_pedras -= pedras_retirada
            return True
        else:
            print(f"Jogada inválida!! \n Você deve retirar entre uma e {self.max_retirada} pedras.")
            return False

    def jogada_maquina(self):
        if self.num_pedras == 1:
            pedras_retirada = 1
        else:
            pedras_retirada = (self.num_pedras - 1) % (self.max_retirada + 1)
            if pedras_retirada == 0:
                pedras_retirada = 1

        print(f"O computador retirou: {pedras_retirada}")
        self.num_pedras -= pedras_retirada

    def verifica_vitoria(self):
        if self.num_pedras == 0:
            if self.turno == 0:
                print("VITÓRIA DO JOGADOR 1!! (JOGADOR 1 RETIROU A ÚLTIMA PEDRA E PERDEU!)")
            else:
                print("VITÓRIA DO JOGADOR 2!! (JOGADOR 2 RETIROU A ÚLTIMA PEDRA E PERDEU!)")
            return True
        return False

    def alterar_turno(self):    
        self.turno = 1 - self.turno

    def jogar(self):
        while self.num_pedras > 0:
            self.exibir_status()

            if self.turno == 0:
                try:
                    pedras_retirada = int(input(f"Quantas pedras você deseja retirar: (1 a {self.max_retirada}): "))
                    if not self.jogada_jogador(pedras_retirada):
                        print(" ")
                    else:
                        if self.num_pedras == 0:
                            print("O JOGADOR 1 RETIROU A ÚLTIMA PEDRA E PERDEU!")
                            break
                        if self.verifica_vitoria():
                            break
                        self.alterar_turno()

                except ValueError:
                    print("Por favor insira um número válido")
                    continue
            else:
                if self.turno == 1 and self.tipo_jogo == 1:
                    try:
                        pedras_retirada = int(input(f"Quantas pedras você deseja retirar: (1 a {self.max_retirada}): "))
                        if not self.jogada_jogador(pedras_retirada):
                            print(" ")
                        else:
                            if self.num_pedras == 0:
                                print("O JOGADOR 2 RETIROU A ÚLTIMA PEDRA E PERDEU!")
                                break
                            if self.verifica_vitoria():
                                break
                            self.alterar_turno()

                    except ValueError:
                        print("Por favor insira um número válido")
                        continue
                else:
                    self.jogada_maquina()
                    if self.num_pedras == 0:
                        print("O COMPUTADOR RETIROU A ÚLTIMA PEDRA E PERDEU!")
                        break
                    if self.verifica_vitoria():
                        break
                    self.alterar_turno()

def iniciar_jogo():
    print("Bem-vindo ao jogo do NIM")
    num_pedras = int(input("Digite o número de pedras: "))
    max_retirada = int(input("Digite o número máximo de pedras que podem ser retiradas por vez: "))
    tipo_jogo = int(input("Você quer jogar contra o (1) Jogador ou (2) Computador? (Digite 1 ou 2): "))

    if tipo_jogo == 1:
        jogo = JogoNim(num_pedras, max_retirada, tipo_jogo)
        jogo.jogar()
    elif tipo_jogo == 2:
        jogo = JogoNim(num_pedras, max_retirada, tipo_jogo)
        jogo.jogar()
    else:
        print("Opção inválida. O jogo será encerrado.")

iniciar_jogo()
