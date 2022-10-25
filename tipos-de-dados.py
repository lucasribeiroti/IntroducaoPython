"""
Tipos de dados:
str - string -> 'Assim' ou "Assim"
int - inteiro -> -1, 2, 3, 4, 5, ... , 100000000...
float - real/ponto flutuante -> 14.0, 1.6, -12.09, ...
bool - booleano/lógico -> true or false 10 == 10
"""
print("Lucas", type("Lucas"))
print(11, type(11))
print(12.0, type(12.0))
print("12.0", type("12.0"))  # qualquer coisa dentro de aspas se torna string.
print(10 == 10, type(10 == 10))
print("l" == "L", type("l" == "L"))
print("Lucas", type("Lucas"), bool("Lucas"))