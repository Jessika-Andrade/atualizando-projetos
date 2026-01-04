
# Leia dois números reais e calcule:
# soma
# subtração
# multiplicação
# divisão
# Mostre todos os resultados. 


n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
sobra = n1 % n2

print(f"A soma de {n1} e {n2} é {soma:.2f}")
print(f"A subtração de {n1} e {n2} é {subtracao:.2f}")
print(f"A Multiplicação de {n1} e {n2} é {multiplicacao:.2f}")
print(f"A Divisão de {n1} e {n2} é {divisao:.2f}")
print(f"A Sobra da divisão de {n1} e {n2} é {sobra:.2f}")