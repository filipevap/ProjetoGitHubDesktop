function pedirSexo(){
    let sexo;
    while (true){
        sexo = prompt("Escreva apenas Masculino, Feminino OU Outro");
        if (sexo === null){
            alert("Cadastro cancelado");
            return null;
        }
        sexo = sexo.trim();
        if(sexo === ""){
            alert("A idade não pode ficar vazia");
            continue;
        }
        if (sexo !== "Masculino" && sexo !== "Feminino" && sexo !== "Outro"){
            alert("Você deve informar apenas se 'Masculino', 'Feminino' ou 'Outro'");
            continue;
        }

        return sexo
    }
}

function iniciarCadastro(){
    let sexo = pedirSexo();
    if (sexo === null){
        document.getElementById("resultado").innerHTML =
            "<h2>Cadastro cancelado</h2>" +
            "<p>O usuário cancelou o preenchimento.</p>";
            return;
    }
    document.getElementById("resultado").innerHTML =
        "<h2>Resultado</h2>" +
        "<p><strong>Sexo: </strong>" + sexo + "</p>"
        
}