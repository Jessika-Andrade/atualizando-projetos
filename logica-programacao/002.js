/* 
O Desafio: Calculadora de Dobro Simples
Crie um programa que:

ENTRADA: Solicite ao usuário que digite um número inteiro.

PROCESSAMENTO: Calcule o dobro desse número.

SAÍDA: Exiba na tela o número original e o seu dobro, em uma frase clara.
*/ 

let numero = Number(prompt("Digite um número: "));
let dobroNumero = numero * 2;

console.log(`Você escolheu o número ${numero}. O dobro é ${dobroNumero}`);
