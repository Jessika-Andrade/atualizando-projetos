/* Média Escolar (Precedência) Um aluno tirou as notas: 7, 8 e 9. Calcule a média final dele.
*/

let nomeAluna = "Beatriz";
let nota1 = 7;
let nota2 = 8;
let nota3 = 9;
let mediaFinal = (nota1 + nota2 + nota3) / 3;

if (mediaFinal >= 7) {
    console.log(`A média final de ${nomeAluna} foi ${mediaFinal}. Aprovado!`)
} else {
    console.log(`A média final de ${nomeAluna} foi ${mediaFinal}. Reprovado!`)
}
