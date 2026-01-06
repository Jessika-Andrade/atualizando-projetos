# Receba um ano.
# Considere bissexto se:
# for divisível por 4
# e não for divisível por 100
# ou
# for divisível por 400
# Retorne True ou False.

ano = input("Ano: ")
int_ano = int(ano)

bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

string_bissexto = f"O ano é bissexto?: {bissexto}"

print(string_bissexto)
