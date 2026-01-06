# Peça a idade de uma pessoa.
# Mostre True se ela for adolescente (entre 13 e 17 anos inclusive), caso contrário False.
# Use apenas operadores relacionais + lógicos.

idade = input("Idade: ")
int_idade = int(idade)

adolescente = int_idade >= 13 and int_idade <= 17

print(f"É adolescente? {adolescente}")