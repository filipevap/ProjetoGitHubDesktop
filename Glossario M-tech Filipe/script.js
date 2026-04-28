function escolheLetra(letraClicada){

    let idBotao = letraClicada.value;
    
    let conteudo = document.getElementById(idBotao).innerHTML;

    document.getElementById("letraselecionada").innerHTML = conteudo;
}