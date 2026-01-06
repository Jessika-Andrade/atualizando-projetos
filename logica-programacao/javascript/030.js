/* Peça:

idade

se a pessoa tem ingresso (True/False)

Uma pessoa só entra se for maior de 18 E tiver ingresso.
Retorne True ou False. */

let idade = prompt("Idade: ");
let intIdade = parseInt(idade);

let temIngresso = prompt("Tem ingresso? [S / N] ").toLowerCase() === "s";

let temPermissao = intIdade >= 18 && temIngresso;

let frasePermissao = `Tem +18 e ingresso? ${temPermissao}`;

console.log(frasePermissao)