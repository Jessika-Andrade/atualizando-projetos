"""
Exercício 1: Você comprou 3 pães (R$ 10.00) e um leite (R$ 5.00). Você pagou com uma nota de R$ 20.00.

Crie variáveis para os itens e para o pagamento.

Calcule o troco.

"""

paes_3_unidades = 10.00
leite = 5.00
total_pedido = paes_3_unidades + leite
pago_dinheiro = 20.00

troco = pago_dinheiro - total_pedido

print(f"3 pães por R${paes_3_unidades:.2f}")
print(f"1 leite por R${leite:.2f}")
print(f"Total do pedido: R${total_pedido:.2f}")
print(f"Foi pago em dinheiro R${pago_dinheiro:.2f}")

if troco > 0:
    print(f"O troco é de R${troco:.2f}.")
elif troco == 0:
    print("O valor pago foi o valor exato do pedido. Não precisa de troco.")
else:
    print("Faltou dinheiro!")