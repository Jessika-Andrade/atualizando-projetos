/* Um dono de loja quer um sistema simples de inventário:
Comece com uma variável estoque = 20.
O dono recebeu uma entrega: adicione 15 unidades ao estoque usando +=.
Houve uma venda de 8 unidades: subtraia usando -=.
O dono quer saber: "O estoque está em um nível seguro?".
A condição de estoque seguro é: Ter mais de 10 unidades E menos de 50 unidades.
Mostre a frase: "Quantidade em estoque: [valor]. Está seguro? [True/False]". */

let estoque = 20;
estoque += 15; // Add 15 unidades
estoque -= 8; // Vendeu 8 unidades.

let estoqueSeguro = estoque > 10 && estoque < 50;
let stringVerificacao = `Quantidade em estoque ${estoque}. Está seguro? ${estoqueSeguro}`;

console.log(stringVerificacao);