/* 
Dado:

h = hora atual (0 a 23)

x = quantidade de horas a somar

Calcule a hora final, respeitando o relógio de 24h.

Exemplo:
h = 22, x = 5 → resultado = 3
*/

let hora = Number(prompt("Digite um horário entre 0 e 23: "));
let horasSomar = Number(prompt("Digite as horas a somar: "));
let horasTotal = (hora + horasSomar) % 24;

console.log(`${hora}h + ${horasSomar}h = ${horasTotal}h.`);