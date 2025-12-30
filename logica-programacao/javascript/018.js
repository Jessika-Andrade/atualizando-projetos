/*
Número palíndromo (sem strings)

Dado um número inteiro positivo de 3 dígitos:

Gere 1 se ele for palíndromo

Gere 0 se não for

Exemplo:
n = 121 → 1
n = 123 → 0
*/

let numero = Number(prompt("Digite um número de três dígitos: "));
let ultimo = numero % 10;
let primeiro = Math.floor(numero / 100);

if (primeiro === ultimo) {
    console.log("1");
} else {
    console.log("0");
}