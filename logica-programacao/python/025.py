# Um banco precisa de um programa que decida se um cliente pode contratar um empréstimo. O cliente será aprovado se atender a pelo menos uma das seguintes condições:

# Condição A: Ter renda mensal maior que R$ 5.000,00 E idade maior ou igual a 21 anos.

# Condição B: Ter renda mensal maior que R$ 3.000,00 E possuir um imóvel próprio (representado por uma variável booleana).

# Além disso, existe uma regra impeditiva (NOT):

# Se o nome do cliente estiver na lista de restrição de crédito (outra variável booleana), ele será reprovado automaticamente, não importa as condições acima.

renda = float(input("Renda: "))
idade = int(input("Idade: "))
tem_imovel = input("Tem imóvel próprio? [Sim / Não] ").lower() == "sim"
tem_restricao = input("Nome sujo? [Sim / Não] ").lower() == "sim"

condicao_a = (renda >= 5000 and idade >= 21)
condicao_b = (renda >= 3000 and tem_imovel)

aprovado = (condicao_a or condicao_b) and not tem_restricao

print(f"O empréstimo foi aprovado?: {aprovado}")