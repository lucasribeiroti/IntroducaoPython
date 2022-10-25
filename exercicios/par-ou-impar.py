"""
Faça um programa que peça para o usuário digitar um número inteiro,
informe se esse número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input("Digite um número: ")

if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print("Esse número é par")
    else:
        print("Esse número é ímpar")
else:
    print("Esse não é um número inteiro")