# Diferença circular
# Dado dois números a e b (0 a 59), representando minutos:
# Calcule a menor diferença entre eles em um relógio
# Exemplo:
# a = 5, b = 55 → diferença = 10

a = int(input("Digite o primeiro número de minutos (0 a 59): "))
b = int(input("Digite o segundo número de minutos (0 a 59): "))

dist_direta = abs(a - b)
dist_circular = 60 - dist_direta

menor_diferenca = min(dist_direta, dist_circular)

print(f"A menor diferença entre {a} e {b} é {menor_diferenca} minutos.")