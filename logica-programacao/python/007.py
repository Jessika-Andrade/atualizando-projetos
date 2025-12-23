"""
Média Escolar (Precedência) Um aluno tirou as notas: 7, 8 e 9. Calcule a média final dele.

"""

nome_aluno = "João"
nota1 = 7
nota2 = 8
nota3 = 9
media_final = (nota1 + nota2 + nota3) / 3

if media_final >= 7:
    print(f"A média final de {nome_aluno} foi {media_final}. Aprovado!")
else:
    print(f"A média final de {nome_aluno} foi {media_final}.Reprovado!")