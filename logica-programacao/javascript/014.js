/*
Dado um número inteiro m (minutos):
Calcule:
Horas completas
Minutos restantes

Exemplo:
m = 187 → 3 horas e 7 minutos */

let numero = Number(prompt("Digite um número em minutos: "));
let horasCompletas = Math.floor(numero / 60);
let minutosRestantes = numero % 60;

console.log(`${numero} -> ${horasCompletas} horas e ${minutosRestantes} minutos.`);