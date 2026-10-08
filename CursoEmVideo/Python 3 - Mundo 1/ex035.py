r1 = int(input("Comprimento reta 1: "))
r2 = int(input("Comprimento reta 2: "))
r3 = int(input("Comprimento reta 3: "))

if r1 + r2 > r2 and r1 + r3 > r2 and r2 + r3 > r1:
    print("Triangulo valido")
else: 
    print("Triangulo invalido")