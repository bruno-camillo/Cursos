s = float(input("Qual é o salário do funcionário? R$"))
a = float(input("Qual é a porcentagem de aumento? "))

ns = s * (1 + a/100)

print("Um funcionario que ganhava R${:.2f}. com {}% de aumento, passa a receber R${:.2f}".format(s, a, ns))