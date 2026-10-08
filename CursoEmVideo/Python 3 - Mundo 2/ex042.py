l1 = int(input("Primeiro lado: "))
l2 = int(input("Segundo lado: "))
l3 = int(input("Terceiro lado: "))

# (l1 == l2 and l1 != l3) or (l1 == l3 and l1 != l3) or (l2 == l3 and l2 != l1):

if l1 + l2 > l2 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 and l1 == l3:
        print("Os segmentos podem formar um triangulo equilatero")
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print("Os segmentos podem formar um triangulo escaleno")
    else:
        print("Os segmentos podem formar um triangulo isoceles")
else: 
    print("Triangulo invalido")