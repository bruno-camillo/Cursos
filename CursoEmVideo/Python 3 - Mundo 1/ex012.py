p = float(input("Qual é o preço do produto? R$"))
d = int(input("Qual é o desconto em porcentagem? "))

np = p * (1 - d/100)

print("O produto custava R${:.2f}, na promoção com desconto de {}% vai custar R${:.2f}".format(p, d, np))

