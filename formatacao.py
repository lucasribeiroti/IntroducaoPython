"""
formatação com .format()
"""
nome = "Lucas"
idade = 23
altura = 1.78  # float sempre separa as casas decimais com ponto
maior_de_idade = idade > 18
peso = 83
imc = peso / altura ** 2

print("{} tem {} anos de idade e seu imc é de {:.2f}".format(nome, idade, imc))
print("{0} tem {1} anos de idade e seu imc é de {2:.2f}".format(nome, idade, imc))  # definindo ordem
print("{n} tem {i} anos de idade e seu imc é de {im:.2f}".format(n=nome, i=idade, im=imc))  # definindo ordem