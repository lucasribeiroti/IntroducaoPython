"""
* Criar variáveis para nome (str), idade (int),
  altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""
nome = "Lucas"
idade = 23
altura = 1.78
peso = 83.90
ano_atual = 2022
data_nasc = ano_atual - idade
imc = peso / (altura ** 2)

print(f"{nome} tem {idade} anos, {altura} de altura e seu peso é de {peso:.2f}kg e seu imc é de {imc:.2f}!")
print(f"Como estamos no ano de {ano_atual}, subtraindo por sua idade, {nome} nasceu em {data_nasc}!")

# Usando o .format
# print("{} tem {} anos, {} de altura e seu peso é {}kg. Seu imc é de {:.2f}!".format(nome, idade, altura, peso, imc))
# print("Como estamos no ano {}, subtraindo por sua idade, {} nasceu em {}!".format(ano_atual, nome, data_nasc))
