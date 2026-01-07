# Enunciado:
# Peça ao usuário o preço de um produto.
# O produto recebeu um aumento de 15%. Atualize a variável do preço usando *=.
# O cliente usou um cupom de desconto de R$ 10,00. Atualize a variável usando -=.
# Mostre uma frase final dizendo: "O valor final é: [valor] " e retorne True se o valor final for maior que 100, ou  False caso contrário.

preco_produto = input("Preço produto: ")
float_preco_produto = float(preco_produto)

float_preco_produto *= 1.15 #Aumento 15%
float_preco_produto -= 10 #Desconto R$10

verificacao = float_preco_produto >= 100

frase_final = f"O valor final é R${float_preco_produto}. É maior que R$100?: {verificacao}"

print(frase_final)