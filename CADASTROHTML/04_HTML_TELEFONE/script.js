function pedirTelefone(){
    let telefone;
    while (true){
        telefone = prompt("Escreva seu número de telefone com DDD. Ex.: DDD999999999");
        if (telefone === null){
            alert("Cadastro cancelado");
            return null;
        }
        telefone = telefone.trim();
        if(telefone === ""){
            alert("O telefone não pode ficar vazio");
            continue;
        }
        let telefone = Number(telefone)
        if (isNaN(telefone) || telefone.length !== 12){
            alert("O telefone deve conter 12 dígitos: 3 para DDD e 9 para linha");
            continue;
        }
        return telefone
    }
}

function iniciarCadastro(){
    let telefone = pedirTelefone();
    if (telefone === null){
        document.getElementById("resultado").innerHTML =
            "<h2>Cadastro cancelado</h2>" +
            "<p>O usuário cancelou o preenchimento.</p>";
            return;
    }
    document.getElementById("resultado").innerHTML =
        "<h2>Resultado</h2>" +
        "<p><strong>Telefone: </strong>" + telefone + "</p>"
        
}