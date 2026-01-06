# Receba um número.
# Mostre True se ele NÃO estiver entre 1 e 100.

numero = input("Número: ")
int_numero = int(numero)

verificacao = not (int_numero >= 1 and int_numero <= 100) 

string_verificacao = f"O número NÃO está entre 1 e 100? {verificacao}"

print(string_verificacao)