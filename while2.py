"""
while em Python, utilizado para realizar ações enquanto
uma condição for verdadeira.
"""
while True:
    num_1 = input("Digite um número: ")
    num_2 = input("Digite outro número: ")
    operador = input("Digite um operador (+, -, / ou *): ")
    sair = input("Deseja sair? S/N: ")

    num_1 = float(num_1)
    num_2 = float(num_2)

    if sair == "S":
        break
    else:
        if operador == "+":
            print(num_1 + num_2)
        else:
            if operador == "-":
                print(num_1 - num_2)
            else:
                if operador == "/":
                    print(num_1 / num_2)
                else:
                    if operador == "*":
                        print(num_1 * num_2)
                    else:
                        print("Opção inválida!")