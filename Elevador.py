# Classe Elevador

class Elevador(object):
     # Método construtor
        def __init__(self, andarAtual, portaAberta, peso):
            self.andarAtual = andarAtual
            self.portaAberta = portaAberta
            self.peso = peso

        def setAndarAtual(self, andarAtual):
            self.andarAtual = andarAtual
        def getAndarAtual(self):
            return self.andarAtual

        def setportaAberta(self, portaAberta):
            self.portaAberta = portaAberta
        def getportaAberta(self):
            return self.portaAberta

        def setpeso(self, peso):
            self.peso = peso
        def getpeso(self):
            return self.peso

        def __str__(self):
            return (
                '\n\t\t Andar Atual ..................' + str(self.getAndarAtual()) +
                '\n\t\t Peso .........................{:.2f}'.format(self.getpeso()) +
                str('\n\t\t -- Porta Aberta --' if self.getportaAberta() else '\n\t\t -- Porta Fechada --')
            )

        def subir(self, andarDesejado):
            if self.fecharPorta():
                while andarDesejado > self.andarAtual:
                    self.andarAtual += 1
                    print(f'{self.andarAtual}º andar')
                self.setportaAberta(True)
            else:
                print('\nElevador Parado. Excesso de peso!')

        def descer(self, andarDesejado):
            if self.fecharPorta():
                while andarDesejado < self.andarAtual:
                    self.andarAtual -= 1
                    print(f'{self.andarAtual}º andar')
                self.setportaAberta(True)
            else:
                print('\nElevador Parado. Excesso de peso!')

        # Método novo - Fechar Porta
        def fecharPorta(self):
            if self.peso < 750:
                self.setportaAberta(False)
            return not self.getportaAberta()