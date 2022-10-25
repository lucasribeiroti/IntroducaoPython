"""
Manipulando strings
* String índices
* Fateamento de strings (inicio:fim:passo)
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.
"""
# positivos [012345678]
# negativos -[987654321]
"""
texto = "Python s2"
print(texto[-8])
"""
texto = "Python_s2"
nova_string = texto[1:6]  # definindo início e fim (se o início for a partir do 0, não precisa colocar o 0)
nova_string2 = texto[0:6:2]  # pulando casas

print(nova_string.upper())
print(nova_string.title())
print(nova_string2)
print(len(texto[0:6:2]))  # contando a quantidade de caracteres da variável "texto" indo do 0 até o 6° caractere pulando 2 casas.

