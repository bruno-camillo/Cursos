name = str(input("Qual seu nome: ")).strip()

print("Seu nome tem Silva? {}".format(name.title().find("Silva") == 0))

# print("Seu nome tem Silva? {}".format( 'silva' in name.lower() ))