# Conversor de base numerica
def convert_bin (i):
    if i < 2:
        return i % 2
    return str(convert_bin(i//2)) + str(i % 2)

def convert_oct (i):
    if i < 8:
        return i % 8
    return str(convert_oct(i//8)) + str(i % 8)

def convert_hex (i):
    if i < 16:
        return i % 16
    return str(convert_hex(i//16)) + " " + str(i % 16)

def transform_hex (num):
    lista = num.strip().split()
    for i, valor in enumerate(lista):
        if valor == "10":
            lista[i] = "a"
        if valor == "11":
            lista[i] = "b"
        if valor == "12":
            lista[i] = "c"
        if valor == "13":
            lista[i] = "d"
        if valor == "14":
            lista[i] = "e"
        if valor == "15":
            lista[i] = "f"
    num = "".join(lista)

    return num

print("-=-"*20)
print("{:^60}".format("CONVERSOR DE BASE NUMERICA"))
print("-=-"*20)

i = int(input("Digite o valor que deseja converter: "))

n = int(input("Digite 1 para converter para binário, 2 para octal e 3 para hexadecimal: "))

if n == 1:
    print(convert_bin(i))
elif n == 2:
    print(convert_oct(i))
elif n == 3:
    i = convert_hex(i)
    i = transform_hex(str(i))
    print(i)
else:
    print("Numero Invalido!")

print("-=-"*20)
