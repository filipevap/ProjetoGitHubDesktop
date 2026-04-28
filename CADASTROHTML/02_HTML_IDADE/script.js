function pedirIdade(){
    let idadeTexto;
    while (true){
        nome = prompt("Digite o seu nome completo:");
        if (nome === null){
            alert("Cadastro cancelado");
            return null;
        }
        idadeTexto - idadeTexto.trim();
        if(idadeTexto ===""){
            alert("A idade não pode ficar vazia");
            continue;
        }

        let idade = Number(idadeTexto);
        if (isNaN(idade) || idade < 0 || !Number.isInteger(idade)){
            alert("Digite uma idade válida usando apenas números inteiros.")
            continue;
        }
        return idade
    }
}

function iniciarCadastro(){
    let idade = pedirIdade();
    if (idade === null){
        document.getElementById("resultado").innerHTML =
            "<h2>Cadastro cancelado</h2>" +
            "<p>O usuário cancelou o preenchimento.</p>";
            return;
    }
    document.getElementById("resultado").innerHTML =
        "<h2>Resultado</h2>" +
        "<p><strong>Nome Completo:</strong>" + nome + "</p>"
        
}