pd = float(input("Qual é o preço por dia? "))
pkm = float(input("Qual é o preço por km rodado? "))

d = int(input("Quantos dias alugados? "))
km = float(input("Quantos quilometros rodados? "))

c = (d*pd) + (km * pkm)

# c = (d*60) + (km * 0.15)

print("O total a pagar é de R${:.2f}".format(c))