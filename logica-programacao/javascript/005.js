/* 
Exercício 2: Você tem 50 balas e quer dividir igualmente entre 4 amigos.
Quantas balas cada amigo recebe?
*/

let quantidadeBalas = 50;
let quantidadeAmigos = 4;

let quantidadesRecebidas = Math.floor(quantidadeBalas / quantidadeAmigos);

let sobra = quantidadeBalas % quantidadeAmigos;

console.log(`A quantidade de balas é: ${quantidadeBalas}`);
console.log(`A quantiadade de amigos é: ${quantidadeAmigos}`);
console.log(`Cada um recebeu: ${quantidadesRecebidas}`);
console.log(`Sobraram ${sobra} no pote`);