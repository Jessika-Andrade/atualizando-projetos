/* Receba um número.
Verifique se ele está entre 10 e 20 (inclusive 10 e 20).
Retorne True ou False. */

let numero = prompt("Número: ");
let floatNumero = parseFloat(numero);

let verificacao = floatNumero >= 10 && floatNumero <= 20;

console.log(`Está entre 10 e 20?: ${verificacao}`);