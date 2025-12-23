/* Leia dois números reais e calcule:
soma
subtração
multiplicação
divisão
Mostre todos os resultados. 
*/

let n1 = Number(prompt("Digite o primeiro número: "));
let n2 = Number(prompt("Digite o segundo número: "));

let soma = n1 + n2;
let subtracao = n1 - n2;
let multiplicacao = n1 * n2;
let divisao = n1 / n2;
let sobra = n1 % n2;

console.log(`A soma de ${n1} e ${n2} é ${soma.toFixed(2)}`);
console.log(`A subtração de ${n1} e ${n2} é ${subtracao.toFixed(2)}`);
console.log(`A Multiplicação de ${n1} e ${n2} é ${multiplicacao.toFixed(2)}`);
console.log(`A Divisão de ${n1} e ${n2} é ${divisao.toFixed(2)}`);
console.log(`A sobra da divisão de ${n1} e ${n2} é ${sobra.toFixed(2)}`);