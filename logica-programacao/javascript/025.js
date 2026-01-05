/* Um banco precisa de um programa que decida se um cliente pode contratar um empréstimo. O cliente será aprovado se atender a pelo menos uma das seguintes condições:

Condição A: Ter renda mensal maior que R$ 5.000,00 E idade maior ou igual a 21 anos.

Condição B: Ter renda mensal maior que R$ 3.000,00 E possuir um imóvel próprio (representado por uma variável booleana).

Além disso, existe uma regra impeditiva (NOT):

Se o nome do cliente estiver na lista de restrição de crédito (outra variável booleana), ele será reprovado automaticamente, não importa as condições acima. */ 

let renda = Number(prompt("Renda: "));
let idade = Number(prompt("Idade: "));
let temImovel = prompt("Tem imóvel? [Sim / Não] ").toLowerCase() === "sim";
let temRestricao = prompt("Nome sujo? [Sim / Não] ").toLowerCase() === "sim";

let condicaoA = (renda >= 5000 && idade >= 21);
let condicaoB = (renda >= 3000 && temImovel);

let aprovado = (condicaoA || condicaoB) && !temRestricao;

console.log(`O empréstimo foi aprovado?: ${aprovado}`)

