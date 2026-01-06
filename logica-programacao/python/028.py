# Receba um número inteiro.
# Retorne True se ele for:
# par ou múltiplo de 5

numero = input("Número: ")
int_numero = int(numero)

verificacao = int_numero % 2 == 0 or int_numero % 5 == 0

print(f"O número é par ou múltiplo de 5? {verificacao}")