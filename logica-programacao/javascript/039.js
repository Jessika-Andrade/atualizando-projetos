/* Enunciado: Crie um sistema de controle de acesso para um elevador de carga:

O elevador começa com peso_atual = 0.

Adicione 3 caixas de 200kg cada (use += ou *).

O elevador só pode subir se atender a DUAS condições ao mesmo tempo:

O peso for maior que 0.

O peso não ultrapassar 500kg.

Crie uma variável pode_subir (booleana) e mostre a frase: "Peso atual: [valor]kg. Pode subir? [True/False]". */

let pesoAtual = 0;
const pesoCaixa = 200;
pesoAtual += (pesoCaixa * 3);

let podeSubir = pesoAtual > 0 && pesoAtual <= 500;

let stringVerificacao = `Peso atual: ${pesoAtual}kg. Pode subir? ${podeSubir}`;

console.log(stringVerificacao);