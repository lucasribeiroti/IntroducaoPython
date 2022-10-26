"""
While / Else
contadores
acumuladores
"""
contador = 1
acumulador = 1

# Exemplo 1
while contador <= 10:
    if contador > 5:
        break
    print(contador, acumulador)
    acumulador += contador  # acumulador é o valor do acumulador + o contador
    contador += 1
else:
    print("Cheguei no else")

"""
Se em algum momento eu sair do laço antes dele acabar (break), o "Cheguei no else" com o comando
else não é executado. Se eu colocar print("Cheguei no else") e não estiver dentro de um else, mesmo se eu
interrompero laço (break), ele será printado na tela.
"""