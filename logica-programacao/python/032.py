# Peça:
# valor da compra
# se é cliente VIP (True/False)
# O desconto é aplicado se:
# compra for maior que 200
# ou
# cliente for VIP
# Retorne True ou False.

valor_compra = input("Valor da compra: R$")
float_valor_compra = float(valor_compra)

cliente_vip = input("Cliente VIP? [S / N] ").lower() == "s"

desconto = float_valor_compra >= 200 or cliente_vip
frase_desconto = f"Cliente ganha desconto? {desconto}"

print(frase_desconto)