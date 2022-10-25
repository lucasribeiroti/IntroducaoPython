"""
Condições IF e ELSE
"""
numero = int(input("Digite um número: "))

if numero < 0:
    print("Esse número é negativo.")
else:
    if numero == 0:
        print("Esse número é neutro.")
    else:
        print("Esse número é positivo.")