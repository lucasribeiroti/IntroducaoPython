"""
+ adição
- subtração
* multiplicação
/ divisão com o resultado ponto flutuante
// divisão com o resultado inteiro (arredondado)
** exponenciação (potênciação)
% retorna o resto da divisão
() altera a precedência
"""
print("10 + 10 =", 10 + 10)  # adição
print("12 - 10 =", 12 - 10)  # subtração
print("10 * 10 =", 10 * 10)  # multiplicação
print(f"11 / 10 = {11 / 6:.2f}")  # divisão com resultado float (:.2f é uma formatação de casas decimais)
print("16 // 10 =", 16 // 7, "(Resultado completo: 2,285714285714286)")  # divisão com resultado int
print("10 ** 2 =", 10 ** 2)  # potenciação
print("10 % 3 =", 10 % 3)  # resto da divisão
print("(10 + 16) / 2 =", (10 + 16) / 2)  # mudando a ordem da operação
print("10 + (16 / 2) =", 10 + (16 / 2))  # mudando a ordem da operação

print("Lucas" + " " + "de" + " " + "Paiva" + " " + "Ribeiro")  # adição de strings
print("Lucas" + " " + "tem" + " " + str(23) + " " + "anos" + "!")  # adição de strings com int formatado em str
