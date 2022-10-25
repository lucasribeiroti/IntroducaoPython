"""
Operadores relacionais:
<, >, <=, >=, ==, !=
"""
expressao = int(input("Digite um número inteiro: "))

if expressao != 0:
    print("O número não é nulo.")
else:
    if expressao == 0:
        print("O número é nulo.")

expressao2 = int(input("Digite outro número inteiro: "))

if expressao2 >= 0:
    print("O número é 0 ou mais.")
else:
    if expressao2 <= 0:
        print("O número é 0 ou menos.")