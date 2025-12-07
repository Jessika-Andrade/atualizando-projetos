/* Escreva um programa que retorne o valor hora de um funcionário com base no seu salário mensal e horas trabalhadas por mês.*/ 

let salarioMensal = Number(prompt("Digite o salário mensal: R$ "));
let horasTrabalhadas = Number(prompt("Digite as horas trabalhadas por mês: "));

if (horasTrabalhadas === 0) {
    console.log("ERRO: O NÚMERO DE HORAS DEVE SER MAIOR QUE ZERO!");
}
else {
    let valorHora = salarioMensal / horasTrabalhadas;
    console.log(`O valor por hora de quem ganha um salário de R$${salarioMensal.toFixed(2)} e trabalhou por ${horasTrabalhadas} horas é R$${valorHora.toFixed(2)}.`);
}
