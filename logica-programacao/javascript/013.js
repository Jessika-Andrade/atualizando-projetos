/*
Dado um número inteiro n:

Gere 1 se for múltiplo de 3

Gere 0 caso contrário
*/ 

let numeroInteiro = Number(prompt("Digite um número inteiro: "));

if (numeroInteiro % 3 === 0) {
    console.log("1");
} else {
    console.log("0");
}

