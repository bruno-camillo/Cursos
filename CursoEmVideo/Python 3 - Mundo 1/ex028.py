import random

n = int(random.randint(0,5))

i = int(input("Qual numero de 0 a 5 a maquina pensou? "))

if n == i:
    print("Voce acertou")
else:
    print("Voce errou")