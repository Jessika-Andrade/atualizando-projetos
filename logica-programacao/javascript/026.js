/* Peça a idade de uma pessoa.
Mostre True se ela for adolescente (entre 13 e 17 anos inclusive), caso contrário False.
Use apenas operadores relacionais + lógicos. */

let idade = prompt("Idade: ");
let intIdade = parseInt(idade);

let adolescente = intIdade >= 13 && intIdade <= 17;

console.log(`Adolescente? ${adolescente}`);