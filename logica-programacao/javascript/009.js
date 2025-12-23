/* Dado um número inteiro positivo n:

Extraia o último dígito

Some esse dígito ao próprio número sem usar strings

Exemplo:
n = 348 → resultado = 348 + 8 = 356 */

let numeroInteiro = Number(prompt("Digite um número inteiro positivo: "));
let ultimoNumero = numeroInteiro % 10;

let resultado = numeroInteiro + ultimoNumero;

console.log(`O número inteiro ${numeroInteiro} + ${ultimoNumero} é ${resultado}`);