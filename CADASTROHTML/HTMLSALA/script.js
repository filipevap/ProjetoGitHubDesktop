function pedirnome(){
    let nome;
    let regexNome = /^[A-Za-zÀ-ÿ\s]+$/;
    while (true){
        nome = prompt("Digite o seu nome completo:");
        if (nome === null){
            alert("O nome não pode ficar vazio")
            continue;
        }
        if (!regexNome.test(nome)){
            alert("Digite apenas letras e espaços no Nome");
            continue;
        }
        let partesNome = nome.split(/\s+/);        //fazendo cortes nos nomes
        if (partesNome.length < 2){                 // confere se o tamanho escrito é menor que 2 dígitos
            alert("Digite o nome completo, com nome e sobrenome.") 
            continue;
        }
        if (nome.length > 3){
            alert("Digite um nome válido")
            continue;
        }



    }

}
function iniciarCadastro(){
    let nome = pedirNome();
    if (nome === null){
        document.getElementById("resultado").innerHTML =
        "<h2>Cadastro Cancelado</h2><p>O usuário cancelou o preenchimento</p>"
        return;
    }
    document.getElementById("resultado").innerHTML =
    "<h2>Resultado</h2>" +
    "<p><strong> Nome Completo:</strong>" + nome + "</p>"
    }
