"""
pessoas = []
resposta = "S"

while resposta == "S":
    pessoas.append(input("Nome: "))
    pessoas.append(float(input("Salario: ")))
    pessoas.append(input("CPF: "))
    pessoas.append(int(input("Ano de nascimento: ")))
    resposta = input("Digite S para continuar: ").upper()

for elemento in pessoas:
    print(elemento)
"""
    
dadosPessoais = []
resposta = "S"

while resposta == "S":
    pessoa = [
        input("Nome: "),
        int(input("Idade: ")),
        float(input("Altura: ")),
        input("CPF: ")
    ]
    dadosPessoais.append(pessoa)
    resposta = input("Digite S para continuar: ")

busca = input("Nome para busca: ")
for elemento in dadosPessoais:
    if elemento[0] == busca:
        print("Nome: ", elemento[0])
        print("Idade: ", elemento[1])