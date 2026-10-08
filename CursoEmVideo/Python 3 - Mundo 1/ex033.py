n1 = int(input("Digite n1: "))
maior = n1

n2 = int(input("Digite n2: "))

if n2 > n1:
    maior = n2

n3 = int(input("Digite n3: "))
if n3 > maior:
    maior = n3

print("o maior numero eh: {}".format(maior))

