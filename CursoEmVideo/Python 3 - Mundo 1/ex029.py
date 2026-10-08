v = int(input("Qual a velocidade resgistrada? "))

if v > 80:
    print("Acima da velocidade. Multa: R${},00".format((v - 80)*7))
else:
    print("Velocidade permitida")