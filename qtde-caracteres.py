"""
len - QUANTIDADE DE CARACTERES
"""

#exemplo1
usuario = input("Digite seu usuário: ")
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print("Você precisa digitar ao menos 6 caracteres para realizar seu cadastro!")
else:
    print("Você foi cadastrado no sistema!")

# exemplo2
string1 = input("Digite alguma coisa: ")
string2 = input("Digite outra coisa: ")

print(f"A quantidade total de caracteres digitados foi {len(string1) + len(string2)}")