/* Dado um número inteiro positivo n com pelo menos dois dígitos:

Obtenha somente o penúltimo dígito

Exemplo:
n = 5729 → resultado = 2 */ 

let numeroInteiro = Number(prompt("Digite um número com pelo menos dois dígitos: "));

let semUltimo = Math.floor(numeroInteiro / 10);
let penultimoNumero = semUltimo % 10;

console.log(`O número ${numeroInteiro} tem como penúltimo ${penultimoNumero}.`);