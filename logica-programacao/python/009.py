# Dado um número inteiro positivo n:

# Extraia o último dígito

# Some esse dígito ao próprio número sem usar strings

# Exemplo:
# n = 348 → resultado = 348 + 8 = 356 


numero_inteiro = int(input("Digite um número inteiro positivo: "))
ultimo_digito = numero_inteiro % 10

resultado = numero_inteiro + ultimo_digito

print(f"O número inteiro {numero_inteiro} + último dígito {ultimo_digito} é {resultado}.")