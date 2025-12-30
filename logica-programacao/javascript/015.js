/* 
Dígito das dezenas

Dado um número inteiro positivo n:

Extraia apenas o dígito das dezenas

Exemplo:
n = 846 → 4 
*/

let numero = Number(prompt("Digite um número com pelo menos 3 dígitos:"));
let dezena = Math.floor(numero / 10);
let extracaoDezena = dezena % 10;

console.log(`Número: ${numero} -> ${extracaoDezena}`);