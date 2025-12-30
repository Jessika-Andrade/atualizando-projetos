"""Dado um número inteiro m (minutos):
Calcule:
Horas completas
Minutos restantes

Exemplo:
m = 187 → 3 horas e 7 minutos"""

numero = int(input("Digite um número em minutos: "))
horas_completas = numero // 60;
minutos_restantes = numero % 60

print(f"{numero} -> {horas_completas} horas e {minutos_restantes} minutos.")
