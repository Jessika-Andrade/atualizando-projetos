/* Peça:
valor da compra
se é cliente VIP (True/False)
O desconto é aplicado se:
compra for maior que 200
ou
cliente for VIP
Retorne True ou False. */

let valorCompra = prompt("Valor da compra: R$ ");
let floatValorCompra = parseFloat(valorCompra);

let clienteVip = prompt("Cliente VIP? [S / N] ").toLowerCase() === "s";

let desconto = floatValorCompra >= 200 || clienteVip;
let fraseDesconto = `Cliente ganha desconto? ${desconto}`;

console.log(fraseDesconto);