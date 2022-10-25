"""
isnumeric, isdigit, isdecimal
"""
num1 = input("Digite um número inteiro: ")
num2 = input("Digite outro número inteiro: ")

# só funciona para tipo int, para float não.
"""
if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(f"{num1} + {num2} = {num1 + num2}")
else:
    print("ERROR")
"""
# formatando direto para float, sem if e else e sim com try e except, agora é possível somar int com float.

try:
    num1 = float(num1)
    num2 = float(num2)
    soma = num1 + num2
    print(f"{num1} + {num2} = {soma}")
except:
    print("ERROR")
