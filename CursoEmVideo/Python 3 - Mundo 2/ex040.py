n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))

m = (n1 + n2)/2

print("Tirando {} e {}, a media do aluno é {}".format(n1, n2, m))

if m >= 7:
    print("Aluno aprovado")
elif m < 7 and m >= 5:
    print("Aluno de recuperação")
else:
    print("Aluno reprovado")