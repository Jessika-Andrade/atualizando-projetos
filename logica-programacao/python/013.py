"""
Dado um número inteiro n:

Gere 1 se for múltiplo de 3

Gere 0 caso contrário

"""

numero_inteiro = int(input("Digite um número inteiro: "))

if numero_inteiro % 3 == 0:
    print("1")
else:
    print("0")