"""
while em Python, utilizado para realizar ações enquanto
uma condição for verdadeira.
"""

# while True:  # loop infinito
#    nome = input("Qual o seu nome? ")
#    print(f"Olá {nome}")

#  exemplo1
x = 0
while x <= 10:  # enquanto x for menor ou igual a 10:
    if x == 3:  # se x é igual a 3: (nesse caso o número 3 será pulado)
        x += 1  # x é igual a x e soma 1 (x += 1 ou x = x + 1)
        continue  # o comando pula um resultado dentro de uma condição
    print(x)
    x += 1
print("Fim!")


# exemplo2
x = 0
while x <= 10:
    if x == 3:
        x = x + 1
        break  # similar ao continue, break termina o laço, finaliza o loop. Então continue pula, break para.
    print(x)
    x = x + 1
print("Fim!")


# exemplo3
x = 0  # coluna
while x < 10:
    y = 0  # linha
    while y <= 9:
        print(f"({x},{y})")
        y += 1
    x += 1

print("Acabou")