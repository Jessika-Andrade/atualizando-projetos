/*
Peça:
usuário
senha
Considere:
usuário correto = "admin"
senha correta = "1234"
Retorne True se usuário e senha forem corretos.
Caso contrário False. */ 

let usuario = prompt("Usuário: ").toLowerCase();
let senha = prompt("Senha: ");
let intSenha = parseInt(senha);

let verificao = usuario === "admin" && intSenha === 1234;
let fraseVerificacao = `Usuário e senha corretos?: ${verificao}`;

console.log(fraseVerificacao);