# Peça:
# idade
# se a pessoa tem ingresso (True/False)
# Uma pessoa só entra se for maior de 18 E tiver ingresso.
# Retorne True ou False.

idade = input("Idade: ")
int_idade = int(idade)

tem_ingresso = input("Tem ingresso? [S / N] ").lower() == "s"

permissao_entrar = int_idade >= 18 and tem_ingresso

frase_permissao = f"Tem +18 e ingresso? {permissao_entrar}"

print(frase_permissao)