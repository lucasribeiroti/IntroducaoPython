"""
while/else
contadores
acumuladores
"""
contador = 1
acumulador = 1
while contador <= 10:
    print(contador, acumulador)
    acumulador += contador
    contador += 1
else:
    print("Cheguei no else!")  # se a condição não for falsa, isso não será printado
print("Acabou!")  # a condição sendo verdadeira ou não, será printado na tela