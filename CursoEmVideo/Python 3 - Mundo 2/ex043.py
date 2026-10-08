p = float(input("Qual o seu peso em quilos? "))

a = float(input("Qual a sua altura em metros? "))

imc = p / (a**2)

print("O IMC é {:.2f}".format(imc))

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso Ideal")
elif imc < 30:
    print("Sobrepeso")
elif imc < 40:
    print("Obesidade")
else:
    print("Obesidade morbida")