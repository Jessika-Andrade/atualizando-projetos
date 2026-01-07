# Peça um número.
# Retorne True se ele não estiver entre 10 e 20 (inclusive).


numero = input("Número: ")
int_numero = int(numero)

verificacao = not (int_numero >= 10 and int_numero <= 20)

string_verificacao = f"O numéro NÃO está entre 10 e 20? {verificacao}"
print(string_verificacao)