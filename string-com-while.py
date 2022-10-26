"""
Iterando strings com while
"""
frase = "Se não tem a manha não entra não"  # são 32 caracteres (do 0 ao 31).
tamanho_frase = len(frase)
contador = 0

while contador <= 31:  # por isso aqui é 31 e não 32, pois começa do 0 e vai até o 31.
    print(frase[contador], contador)
    contador += 1

