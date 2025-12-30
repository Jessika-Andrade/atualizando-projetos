/*
Verificação de paridade 

Dado um número inteiro n:

Gere o valor 1 se o número for ímpar

Gere o valor 0 se for par
*/

let numeroInteiro = Number(prompt("Digite um número: "));
let verificacao = numeroInteiro % 2;

if (verificacao === 1) {
    console.log("1");
} else {
    console.log("0");
}