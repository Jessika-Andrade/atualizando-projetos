# Dígito das dezenas
# Dado um número inteiro positivo n:
# Extraia apenas o dígito das dezenas
# Exemplo:
# n = 846 → 4

numero = int(input("Escreva um número com pelo menos 3 dígitos: "))
dezena = numero // 10
extracao_dezena = dezena % 10

print(f"Número = {numero} -> {extracao_dezena}")