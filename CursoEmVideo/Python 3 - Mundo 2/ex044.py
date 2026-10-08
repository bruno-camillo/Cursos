p = float(input("Digite o valor: R$"))

o = int(input("""Forma de pagamento 
[1] à vista dinheiro/cheque
[2] à vista cartao
[3] 2x no cartao
[4] 3x ou mais no cartao
Selecione a opção: """))

if o == 1:
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(p, p*0.9))
elif o == 2:
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(p, p*0.95))
elif o == 3:
    print("Sua compra vai ser parcelada em 2x de R${:.2f} sem juros".format(p/2))
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(p, p))
elif o == 4:
    n = int(input("Quantas parcelas? "))
    j = p*1.2
    print("Sua compra vai ser parcelada em {}x de R${:.2f} com juros simples de 20%".format(n, j/n))
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(p, j))
else:
    print("Opção invalida")
