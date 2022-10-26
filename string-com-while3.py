"""
Iterando strings com while
"""
frase = "Se não tem a manha não entra não"  # Iteráveis, são 32 caracteres (do 0 ao 31)
tamanho_frase = len(frase)
contador = 0
nova_string = ""

usuario = input("Digite a letra que deseja colocar em maiúscula: ")

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == usuario:
        nova_string += usuario.upper()  # upper é uma função dentro da string que converte a letra pra maiúsculo.
    else:
        nova_string += letra
    contador += 1
print(nova_string)