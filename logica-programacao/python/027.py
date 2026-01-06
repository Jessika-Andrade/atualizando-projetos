# Receba um número.
# Verifique se ele está entre 10 e 20 (inclusive 10 e 20).
# Retorne True ou False.

numero = input("Número: ")
float_numero = float(numero)

verificacao = float_numero >= 10 and float_numero <= 20

print(f"Está entre 10 e 20?: {verificacao}")