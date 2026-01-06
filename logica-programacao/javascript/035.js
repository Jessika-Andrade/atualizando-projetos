/* Receba um ano.
Considere bissexto se:

for divisível por 4
e não for divisível por 100
ou

for divisível por 400

Retorne True ou False. */

let ano = prompt("Ano: ");
let intAno = parseInt(ano);

let bissexto = (intAno % 4 === 0 && intAno % 100 !== 0) || (intAno % 400 === 0);

let stringBissexto = `O ano é bissexto? ${bissexto}`;
console.log(stringBissexto);