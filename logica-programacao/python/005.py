"""
Exercício 2: Você tem 50 balas e quer dividir igualmente entre 4 amigos.
Quantas balas cada amigo recebe?

"""

quantidade_balas = 50
quantidade_amigos = 4

quantidade_recebida = quantidade_balas // quantidade_amigos
sobra = quantidade_balas % quantidade_amigos

print(f"Quantidade de balas a serem divididas: {quantidade_balas}")
print(f"Quantidade de amigos: {quantidade_amigos}")
print(f"Cada um vai receber: {quantidade_recebida}")
print(f"Sobraram {sobra} balas no pote")