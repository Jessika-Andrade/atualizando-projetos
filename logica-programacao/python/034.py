# Peça duas notas.
# A pessoa é aprovada se:
# média ≥ 7 ou média ≥ 6 E nenhuma nota é menor que 5
# Retorne True ou False.

nota_1 = input("Nota 1: ")
float_nota_1 = float(nota_1)

nota_2 = input("Nota 2: ")
float_nota_2 = float(nota_2)

media = (float_nota_1 + float_nota_2) / 2

aprovado = (media >= 7) or (media >= 6 and float_nota_1 >= 5 and float_nota_2 >= 5)

string_aprovado = f"Aluno aprovado? {aprovado}"

print(string_aprovado)