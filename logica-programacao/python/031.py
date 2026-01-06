# Peça:
# usuário
# senha
# Considere:
# usuário correto = "admin"
# senha correta = "1234"
# Retorne True se usuário e senha forem corretos.
# Caso contrário False.

usuario = input("Usuário: ").lower()
senha = input("Senha: ")
int_senha = int(senha)

verificacao = usuario == "admin" and int_senha == 1234
frase_verificao = f"Usuário e senha corretos?: {verificacao}"

print(frase_verificao)