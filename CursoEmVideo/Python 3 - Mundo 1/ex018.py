import math

ang = float(input("Digite um angulo: "))

# valor do angulo precisa estar em radianos
ang = math.radians(ang)

print("SENO = {:.2f}".format(math.sin(ang)))
print("COSSENO = {:.2f}".format(math.cos(ang)))
print("TANGENTE = {:.2f}".format(math.tan(ang)))