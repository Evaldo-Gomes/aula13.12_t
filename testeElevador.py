# Classe de Teste para a classe Elevador
import random

from Elevador import Elevador

# Criação da instância do objeto

e1 = Elevador(0, True, random.random() * 1000)

# Exibindo o elevador parado
print('\n\t\t -- Elevador no Térreo --')
print(e1)

# Subindo...
e1.subir(5)

# Imprimindo o status do elevador no 5º andar
print('\n\t\t -- Elevador no 5º Andar --')
print(e1)

# Descendo...
e1.descer(0)

# Imprimindo o status do elevador no Térreo
print('\n\t\t -- Elevador no Térreo --')
print(e1)