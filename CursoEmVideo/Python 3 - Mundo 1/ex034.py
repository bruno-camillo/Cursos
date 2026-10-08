s = float(input("Qual seu salario? "))

if s > 1250.0:
    print("Seu novo salario eh de R${:.2f}".format(s*1.1))
else:
    print("Seu novo salario eh de R${:.2f}".format(s*1.15))
