/* 
Diferença circular

Dado dois números a e b (0 a 59), representando minutos:

Calcule a menor diferença entre eles em um relógio

Exemplo:
a = 5, b = 55 → diferença = 10
 
*/ 

let a = Number(prompt("Digite o primeiro número de minutos (0 a 59): "));
let b = Number(prompt("Digite o primeiro número de minutos (0 a 59): "));

let distDireta = Math.abs(a - b);
let distCircular = 60 - distDireta;

let menorDiferenca = Math.min(distDireta, distCircular);

console.log(`A menor diferença entre ${a} e ${b} é ${menorDiferenca} minutos.`);
