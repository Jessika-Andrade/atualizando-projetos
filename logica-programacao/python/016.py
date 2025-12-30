"""
Dado:

h = hora atual (0 a 23)

x = quantidade de horas a somar

Calcule a hora final, respeitando o relógio de 24h.

Exemplo:
h = 22, x = 5 → resultado = 3
"""

hora = int(input("Digite um horário entre 0 e 23: "))
horas_somar = int(input("Digite as horas a somar: "))

horas_total = (hora + horas_somar) % 24 


print(f"{hora}h + {horas_somar}h = {horas_total}h.")
