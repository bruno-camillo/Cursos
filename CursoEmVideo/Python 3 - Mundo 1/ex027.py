n = input("Digite seu nome: ").strip().title()

l = n.split()

print("muito prazer")

i = len(l) - 1

print("Seu primeiro nome eh {}".format(l[0]))

print("Seu Ultimo nome eh {}".format(l[i]))