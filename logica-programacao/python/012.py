"""
Verificação de paridade 

Dado um número inteiro n:

Gere o valor 1 se o número for ímpar

Gere o valor 0 se for par
"""

numero_inteiro = int(input("Digite um número: "))
verificacao = numero_inteiro % 2

if verificacao == 1:
    print(f"1")
else: 
    print(f"0")