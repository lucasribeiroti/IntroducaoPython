"""
Iterando strings com while
"""
frase = "Se não tem a manha não entra não"  # são 32 caracteres (do 0 ao 31).
tamanho_frase = len(frase)
contador = 0

while contador < tamanho_frase:
    print(frase[contador], contador)
    contador += 1

