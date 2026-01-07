# Enunciado: Crie um sistema de controle de acesso para um elevador de carga:
# O elevador começa com peso_atual = 0.
# Adicione 3 caixas de 200kg cada (use += ou *).
# O elevador só pode subir se atender a DUAS condições ao mesmo tempo:
# O peso for maior que 0.
# O peso não ultrapassar 500kg.
# Crie uma variável pode_subir (booleana) e mostre a frase: "Peso atual: [valor]kg. Pode subir? [True/False]".

peso_atual = 0
peso_caixa = 200
peso_atual += (peso_caixa * 3)

pode_subir = peso_atual > 0 and peso_atual <= 500

string_verificacao = f"Peso atual: {peso_atual}kg. Pode subir? {pode_subir}"

print(string_verificacao)