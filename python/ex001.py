"""
Identifique o Tipo : Para cada um dos valores a seguir, atribua-o a uma variável e use a type()função para determinar seu tipo de dado. Imprima o valor e seu tipo.

150
42.0
"Aprender Python é divertido!"
False
[10, 20, 30]
{'city': 'New York', 'population': 8000000}
None(Este é um valor especial do Python que representa a ausência de um valor, ele tem seu próprio tipo NoneType)
"""

idade_idoso = 150
print(f"Valor de idade_idoso: {idade_idoso}")
print(f"Tipo de idade_idoso: {type(idade_idoso)}\n")

preco_produto = 42.0
print(f"Valor de preco_produto: {preco_produto}")
print(f"Tipo de preco_produto: {type(preco_produto)}\n")

frase = "Aprender Python é divertido!"
print(f"Valor de frase: {frase}")
print(f"Tipo de frase: {type(frase)}\n")

usuario_inativo = False
print(f"Valor de usuario_inativo: {usuario_inativo}")
print(f"Tipo de usuario_inativo: {type(usuario_inativo)}\n")

notas = [10, 20, 30]
print(f"Valor de notas: {notas}")
print(f"Tipo de notas: {type(notas)}\n")

informacoes_geograficas = {"city": "New York", "population": 8000000}
print(f"Valor de informacoes_geograficas: {informacoes_geograficas}")
print(f"Tipo de informacoes_geograficas: {type(informacoes_geograficas)}\n")

sem_valor = None
print(f"Valor de sem_valor: {sem_valor}")
print(f"Tipo de sem_valor: {type(sem_valor)}")
