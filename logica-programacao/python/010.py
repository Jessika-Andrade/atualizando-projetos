"""
Dado um número inteiro positivo n com pelo menos dois dígitos:

Obtenha somente o penúltimo dígito

Exemplo:
n = 5729 → resultado = 2

"""

numero_inteiro = int(input("Digite um número com pelo menos dois digitos: "))

sem_ultimo = numero_inteiro // 10
penultimo_numero = sem_ultimo % 10

print(f"O número {numero_inteiro} tem como penúltimo {penultimo_numero}.")