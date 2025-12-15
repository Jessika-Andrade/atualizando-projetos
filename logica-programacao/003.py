"""
Crie um programa que:

ENTRADA: Solicite ao usuário que digite um número inteiro.

PROCESSAMENTO (com Decisão):

Verifique se o número é par ou ímpar. 

SAÍDA: Exiba uma mensagem clara dizendo se o número digitado é "PAR" ou "ÍMPAR".

"""

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")
