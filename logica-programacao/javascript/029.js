/* Receba um número. Retorne True se ele: for par e maior que 50. Caso contrário, False. */

let numero = prompt("Número: ");
let floatNumero = parseFloat(numero);

let verificacao = floatNumero % 2 === 0 && floatNumero > 50;

let fraseVerificacao = `É par e maior que 50? ${verificacao}`;

console.log(fraseVerificacao);