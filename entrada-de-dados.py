"""
Entrada de dados: input
"""
nome_exemplo = input("Qual o seu nome? ")
idade_exemplo = input("Qual a sua idade? ")
ano_atual_exemplo = input("Em que ano estamos..? ")

data_nasc = (int(ano_atual_exemplo) - int(idade_exemplo))

print(f"{nome_exemplo} tem {idade_exemplo} anos e seu ano de nascimento é de {data_nasc}")


# definir tipo de variável junto com input

nome_exemplo2 = str(input("Qual o seu nome? "))
idade_exemplo2 = int(input("Qual sua idade? "))
ano_atual_exemplo2 = int(input("Em que ano estamos..? "))

data_nasc2 = (ano_atual_exemplo2 - idade_exemplo2)

print(f"{nome_exemplo2} tem {idade_exemplo2} anos e seu ano de nascimento é de {data_nasc2}")
