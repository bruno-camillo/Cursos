print("Hello World!")

# Comentario de uma linha

"""
Comentario
de
mais
de 
uma
linha
"""

n = int(input("Digite um numero de 1 a 10: "))
print(n)

print (type(n))

if n > 10 : 
    print("o numero eh maior que 10")
elif n < 10: 
    print("O numero eh menor a 10")
else:
    print("O numero eh igual a 10")

i = 0

while i < 10:
    print(i)
    i = i + 1

def function (a, b):
    if a > b:
        print(a + b)
    elif a < b:  
        print(a - b)
    else:
        print(a * b)


a = int(input("Digite um valor para a: "))
b = int(input("Digite um valor para b: "))

function(a, b)

for i in range(1, 11, 1):
    print ("O valor eh: " + str(i))

lista = [1, 2, 3]

for i in range(0, 3, 1):
    print(lista[i])
    lista.append(i)

print(lista)


