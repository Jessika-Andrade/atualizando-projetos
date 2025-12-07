"""
Calcular o Índice de Massa Corporal (IMC): Escreva um programa que receba o peso de uma pessoa em quilogramas (float) e a altura em metros (float) como entrada e calcule seu IMC. O IMC é calculado como peso / (altura * altura).

"""
peso = float(input("Digite seu peso em quilos: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2) 

if imc > 0:

    if imc < 18.5:
        print(f"IMC: {imc:.2f}KG. Abaixo do peso normal!")
    elif imc <= 24.9:
        print(f"IMC: {imc:.2f}KG. Peso normal!")
    elif imc <= 29.9:
        print(f"IMC: {imc:.2f}KG. Excesso de peso!")
    elif imc <= 34.9:
        print(f"IMC: {imc:.2f}KG. Obesidade nível 1")
    elif imc <= 39.9:
        print(f"IMC: {imc:.2f}KG. Obesidade nível 2.")
    else:
        print(f"IMC: {imc:.2f}KG. Obesidade nível 3.")

else: 
    print(f"INVÁLIDO! TENTE NOVAMENTE COM AS INFORMAÇÕES CORRETAS!")