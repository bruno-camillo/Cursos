v = float(input("Qual o valor da casa? "))
s = float(input("Qual o seu salario? "))
a = int(input("Qual o prazo das prestações? "))

p = v / (a * 12) #prestação mensal

if p > s * 0.3:
    print("Emprestimo negado!!!")
else:
    print("""Seu emprestimo foi aprovado! 
             Será pago prestações de R${:.2f} em {} meses sem juros!""".format(p, a*12))