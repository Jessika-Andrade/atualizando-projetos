# Escreva um programa que retorne o valor hora de um funcionário com base no seu salário mensal e horas trabalhadas por mês.

#Temos que fazer o seguinte cálculo:
# salario mensal / total de horas trabalhadas

salario_mensal = float(input("Qual o seu salário mensal? R$ "))
horas_trabalhadas = float(input("Quantas horas trabalhadas? "))

if horas_trabalhadas == 0:
    print("ERRO: O NÚMERO DE HORAS DEVE SER MAIOR QUE 0!")
else:
    valor_hora = salario_mensal / horas_trabalhadas
    print(f"O valor hora de um funcionário que recebe R${salario_mensal:.2f} e trabalha {horas_trabalhadas} por mês é R${valor_hora:.2f}")