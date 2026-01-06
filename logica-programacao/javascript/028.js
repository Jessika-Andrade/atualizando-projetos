/* Receba um número inteiro.
Retorne True se ele for:
par ou múltiplo de 5
 */

let numero = prompt("Número: ");
let intNumero = parseInt(numero);

let verificacao = intNumero % 2 === 0 || intNumero % 5 === 0;

console.log(`O número é par ou múltiplo de 5? ${verificacao}`);