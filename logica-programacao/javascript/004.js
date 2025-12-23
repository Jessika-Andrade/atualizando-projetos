/* 
Exercício 1: Você comprou 3 pães (R$ 10.00) e um leite (R$ 5.00). Você pagou com uma nota de R$ 20.00.

Crie variáveis para os itens e para o pagamento.

Calcule o troco.
*/

let paes = 10.00;
let leite = 5.00;
let totalPedido = paes + leite;
let pago = 20.00;

let troco = pago - totalPedido;

console.log(`3 unidades de pães por R$${paes.toFixed(2)}`);
console.log(`1 leite por R$${leite.toFixed(2)}`);
console.log(`Total de pedido: R$${totalPedido.toFixed(2)}`);
console.log(`Pago em dinheiro: R$${pago.toFixed(2)}`);

if (troco > 0) {
    console.log(`O troco é de R$${troco.toFixed(2)}`);
} else if (troco === 0) {
    console.log("O valor pago foi o valor exato do pedido. Não precisa de troco.");
} else {
    console.log("Faltou dinheiro!");
}