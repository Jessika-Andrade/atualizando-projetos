/* Enunciado:

Peça ao usuário o preço de um produto.

O produto recebeu um aumento de 15%. Atualize a variável do preço usando *=.

O cliente usou um cupom de desconto de R$ 10,00. Atualize a variável usando -=.

Mostre uma frase final dizendo: "O valor final é: [valor]" e retorne True se o valor final for maior que 100, ou False caso contrário. */ 

let precoProduto = prompt("Preço produto: ");
let floatPrecoProduto = parseFloat(precoProduto);

floatPrecoProduto *= 1.15; // Aumento 15%
floatPrecoProduto -= 10; // Desconto R$10

let verificacao = floatPrecoProduto >= 100;

let fraseFinal = `O valor final é R$${floatPrecoProduto}. É maior que R$100?: ${verificacao}`;