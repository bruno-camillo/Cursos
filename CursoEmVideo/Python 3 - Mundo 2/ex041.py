a = int(input("Ano de nascimento: "))

i = 2026 - a

print("Atleta tem {} anos".format(i))

if i <= 9:
    print("Atleta mirim")
elif i <= 14:
    print("Atleta infantil")
elif i <= 19:
    print("Atleta junior")
elif i <= 25:
    print("Atleta senior")
else:
    print("Atleta master")