"""
Pense em um pedido online simples. Que tipos de dados você usaria para representar as seguintes informações?

ID do pedido (por exemplo, ORD12345)
Custo total (por exemplo, 55.75)
Número de itens (por exemplo, 3)
Endereço de e-mail do cliente (por exemplo, "customer@example.com")
O pedido foi enviado? (Sim/Não)
Lista de itens no pedido (por exemplo, ["Laptop", "Mouse", "Keyboard"])
Escreva um código Python para criar variáveis para cada uma delas, atribua valores de exemplo e, em seguida, imprima o valor de cada variável e seu tipo inferido usando type().

"""

id_pedido = "ORD12345"
custo_total = 55.75
numero_itens = 3
email = "customer@example.com"
pedido_enviado = True
lista_itens_pedido = ["Notebook", "Mouse", "Teclado"]

print(f"ID do pedido: {id_pedido}. Tipo: {type(id_pedido)}\n")
print(f"Custo total: R${custo_total}. Tipo: {type(custo_total)}\n")
print(f"Número de itens: {numero_itens}. Tipo: {type(numero_itens)}\n")
print(f"E-mail do cliente: {email}. Tipo: {type(email)}\n")
print(f"O pedido foi enviado? {pedido_enviado}. Tipo: {type(pedido_enviado)}\n")
print(f"Itens do pedido: {lista_itens_pedido}. Tipo: {type(lista_itens_pedido)}\n")
