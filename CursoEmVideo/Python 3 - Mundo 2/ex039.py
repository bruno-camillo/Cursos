a = int(input("Digite seu ano de nascimento: "))
i = 2026 - a
print("Quem nasceu em {} tem {} anos em 2026".format(a, i))

if i < 18:
    print("Ainda faltam {} anos para o seu alistamento".format(18 - i))
    print("O seu alistamento será em {}".format(2026 + 18 - i))
elif i > 18:
    dif = i - 18
    if dif == 1:
        print("Você já deveria ter se alistado há 1 ano")
    else:
        print("Você já deveria ter se alistado há {} anos".format(dif))
    print("Seu alistamento foi em {}".format(2026 - dif))
else:
    print("Você deve se alistar esse ano!")