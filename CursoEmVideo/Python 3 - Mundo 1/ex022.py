nome = str(input("Digite o seu nome: "))

print(nome.upper())
print(nome.lower())

print(len(nome.replace(" ", "")))

listaNome = nome.split()

print(listaNome)
print(len(listaNome[0]))