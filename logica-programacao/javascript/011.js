/* 
Soma dos dígitos de um número de 3 dígitos

Dado n (100 a 999):

Calcule a soma dos seus dígitos

Apenas operadores aritméticos

Exemplo:
n = 384 → 3 + 8 + 4 = 15 
*/ 

let numeroTresDigitos = Number(prompt("Digite um número com três dígitos: "));
let numeroDoisDigitos = Math.floor(numeroTresDigitos / 10);
let numeroUmDigito = Math.floor(numeroDoisDigitos / 10);

console.log(`${numeroTresDigitos}, ${numeroDoisDigitos}, ${numeroUmDigito}`);

let ultimoNumero = numeroTresDigitos % 10;
let penultimoNumero = numeroDoisDigitos % 10;
let antepenultimoNumero = numeroUmDigito % 10;

let soma = ultimoNumero + penultimoNumero + antepenultimoNumero;

console.log(`${ultimoNumero} + ${penultimoNumero} + ${antepenultimoNumero} = ${soma}`);