n = int(input("Digite um número para ver sua tabuada: "))

print("-"*14)

for i in range (1, 11, 1):
    print("{} x {:<2} = {}".format(n, i, n*i))

print("-"*14)