d = int(input("Qual a distancia da viagem? "))

if d <= 200:
    print("O preço da passagem eh de R${:.2f}".format(d*0.5))
else:
    print("O preço da passagem eh de R${:.2f}".format(d*0.45))
