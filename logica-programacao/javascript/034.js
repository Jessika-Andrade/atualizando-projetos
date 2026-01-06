/* Peça duas notas.
A pessoa é aprovada se:

média ≥ 7
ou

média ≥ 6 E nenhuma nota é menor que 5

Retorne True ou False. */ 

let nota1 = prompt("Nota 1: ");
let floatNota1 = parseFloat(nota1);

let nota2 = prompt("Nota 2: ");
let floatNota2 = parseFloat(nota2);

let media = (floatNota1 + floatNota2) / 2;

let aprovado = (media >= 7) ||( media >= 6 && floatNota1 >= 5 && floatNota2 >= 5);

let stringAprovado = `Aluno aprovado? ${aprovado}`;

console.log(stringAprovado);