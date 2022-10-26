"""
while em Python, utilizado para realizar ações enquanto
uma condição for verdadeira.
"""
while True:
    num_1 = input("Digite um número: ")
    num_2 = input("Digite outro número: ")
    operador = input("Digite um operador (+, -, / ou *): ")


    num_1 = float(num_1)
    num_2 = float(num_2)

    soma = (num_1 + num_2)
    subtracao = (num_1 - num_2)
    multiplicacao = (num_1 * num_2)
    divisao = (num_1 / num_2)

    if operador == "+":
        print(soma)
        sair = input("Deseja sair? [s]im ou [n]ão: ")
        if sair == "s":
            print("Até logo!")
            break
    else:
        if operador == "-":
            print(subtracao)
            sair = input("Deseja sair? [s]im ou [n]ão: ")
            if sair == "s":
                print("Até logo!")
                break
        else:
            if operador == "/":
                print(divisao)
                sair = input("Deseja sair? [s]im ou [n]ão: ")
                if sair == "s":
                    print("Até logo!")
                    break
            else:
                if operador == "*":
                    print(multiplicacao)
                    sair = input("Deseja sair? [s]im ou [n]ão: ")
                    if sair == "s":
                        print("Até logo!")
                        break
                else:
                    print("Operador inválido!")