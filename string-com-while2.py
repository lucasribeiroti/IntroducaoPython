"""
Iterando strings com while
"""
frase = "Se não tem a manha não entra não"  # são 32 caracteres (do 0 ao 31).
tamanho_frase = len(frase)
contador = 0
nova_string = ""

while contador < tamanho_frase:
    nova_string += frase[contador]
    print(nova_string)
    contador += 1
