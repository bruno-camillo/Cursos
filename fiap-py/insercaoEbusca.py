def buscaMaior (list): 
    maior = -1
    for i in range (0, len(list), 1):
        if list[i] > maior:
            maior = list[i]
    return maior

lista = []
n = int(input("Digite um natural a ser inserido (-1 acaba com a lista): "))
while n != -1:
    lista.append(n) 
    n = int(input("Digite um natural a ser inserido (-1 acaba com a lista): "))

maior = buscaMaior(lista)

print(lista)
print(maior)

print(max(lista))
