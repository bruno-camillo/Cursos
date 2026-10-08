#Verifica se a cidade digitada começa com Santo ... 

c = str(input("Qual cidade vc nasceu: ")).strip()

l = c.split()

print(l[0].upper() == "SANTO")