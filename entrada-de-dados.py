"""
Entrada de dados: input
"""
nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")
ano_atual = int(input("Em que ano estamos..? "))

data_nasc = ano_atual - int(idade)

print(f"{nome} tem {idade} anos e seu ano de nascimento é de {data_nasc}")