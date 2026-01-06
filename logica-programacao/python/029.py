# Receba um número. Retorne True se ele: for par e maior que 50. Caso contrário, False.

numero = input("Número: ")
float_numero = float(numero)

verificacao = float_numero % 2 == 0 and float_numero > 50

frase_verificacao = f'É par e maior que 50? {verificacao}'

print(frase_verificacao)