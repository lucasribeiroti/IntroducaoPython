"""
Operadores lógicos:
and, or, not, in e not in
"""

# exemplo 1
expressao = int(input("Digite um número inteiro: "))

if expressao != 0 and expressao > 0:
    print("O número não é nulo e é positivo.")
else:
    if expressao != 0 and expressao < 0:
        print("O número não é nulo e é negativo.")
    else:
        if expressao == 0:
            print("O número é nulo.")

# exemplo 2
nome = input("Qual seu nome? ")

if "u" in nome:
    print("Existe a letra U no nome.")
else:
    print("Não existe a letra U no nome.")


# exemplo3

if "u" not in nome:
    print("Não existe a letra U no nome.")
else:
    print("Existe a letra U no nome.")
