"""
Número palíndromo (sem strings)

Dado um número inteiro positivo de 3 dígitos:

Gere 1 se ele for palíndromo

Gere 0 se não for

Exemplo:
n = 121 → 1
n = 123 → 0
"""

numero = int(input("Digite um número de três dígitos: "))
ultimo = numero % 10
primeiro = numero // 100

if primeiro == ultimo:
    print("1")
else: 
    print("0")