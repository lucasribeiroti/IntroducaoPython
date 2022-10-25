"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex: Bom dia 00-11, Boa tarde 12-17,
Boa noite 18-23, caso contrário digite "Hora inválida"
"""
hora = input("Digite a hora: ")

if hora.isdigit():
    hora = int(hora)
    if hora < 00 or hora > 23:
        print("Hora inválida!")
    else:
        if hora <= 11:
            print("Bom dia!")
        else:
            if hora <= 17:
                print("Boa tarde!")
            else:
                print("Boa noite!")
else:
    print("Hora inválida!")
