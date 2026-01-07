/* Peça um número.
Retorne True se ele não estiver entre 10 e 20 (inclusive). */ 

let numero = prompt("Número: ");
let intNumero = parseInt(numero);

let verificacao = !(intNumero >= 10 && intNumero <= 20);

let stringVerificacao = `O número NÃO está entre 10 e 20? ${verificacao}`;
console.log(stringVerificacao);
