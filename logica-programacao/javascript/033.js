/* Receba um número.
Mostre True se ele NÃO estiver entre 1 e 100.
 */

let numero = prompt("Número: ");
let intNumero = parseInt(numero);

let verificacao = !(intNumero >= 1 && intNumero <= 100);

let stringVerificacao = `O número NÃO está entre 1 e 100? ${verificacao}`;

console.log(stringVerificacao)