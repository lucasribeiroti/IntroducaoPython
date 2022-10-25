"""
Variável - iniciar com letra, pode conter números, separar por _, letras minúsculas
"""
nome = "Lucas"
idade = 23
altura = 1.78  # float sempre separa as casas decimais com ponto
maior_de_idade = idade > 18
peso = 83
imc = peso / altura ** 2

print(nome, type(nome))
print(idade, type(idade))
print(altura, type(altura))
print(maior_de_idade, type(maior_de_idade))

# duas formas de se fazer:
print(f"O índice de massa corporal de {nome} é de: {imc:.1f}")  # mais recomendada
print("O índice de massa corporal de", (nome), "é de:",  (peso / altura ** 2))  # menos recomendada