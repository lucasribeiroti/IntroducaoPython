"""
Formatando valores com modificadores;
:s - Texto (strings)
:d - Inteiros (int)
:f - Pontos flutuantes (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)
> - Esquerda
< - Direita
^ - Centro
"""
numero_1 = 10
numero_2 = 3
divisao = numero_1 / numero_2

print(f"{numero_1} / {numero_2} = {divisao:.2f}")  # definindo quantidade de casas decimais (:.2f)
print(f"{numero_1:0>10}")
print(f"{numero_1:0<10}")
print(f"{numero_1:0^10}")
print(f"{numero_1:0>10.2f}")

nome = "lucas ribeiro"
print(nome.lower())  # tudo minúsculo
print(nome.upper())  # tudo maiúsculo
print(nome.title())  # primeiras letras maiúsculas