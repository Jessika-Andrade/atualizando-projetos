
# Soma dos dígitos de um número de 3 dígitos
# Dado n (100 a 999):
# Calcule a soma dos seus dígitos
# Apenas operadores aritméticos
# Exemplo:
# n = 384 → 3 + 8 + 4 = 15# 

numero_tres_digitos = int(input("Digite um número com três dígitos: "))
numero_dois_digitos = numero_tres_digitos // 10
numero_um_digito = numero_dois_digitos // 10

print(f"{numero_tres_digitos}, {numero_dois_digitos}, {numero_um_digito}")

ultimo_numero = numero_tres_digitos % 10
penultimo_numero = numero_dois_digitos % 10
antepenultimo_numero = numero_um_digito % 10

soma = ultimo_numero + penultimo_numero + antepenultimo_numero

print(f"{ultimo_numero} + {penultimo_numero} + {antepenultimo_numero} = {soma}")
