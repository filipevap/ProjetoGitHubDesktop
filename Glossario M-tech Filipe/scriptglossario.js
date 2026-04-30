function escolheLetra(letraClicada) {
    let botaoClicado = letraClicada.id;
    let nomeDaLetra = botaoClicado.slice(-1);

    let conteudo = document.getElementById(nomeDaLetra).innerHTML;

    let cardLetraSelecionada = document.getElementById("letraselecionada");

    cardLetraSelecionada.innerHTML = conteudo;
    cardLetraSelecionada.style.display = "block";
}

function fechaCard(){
    document.getElementById("letraselecionada").style.display = "none";
}

function botaoPesquisar() {

    let termoPesquisa = document
        .getElementById("palavrapesquisada")
        .value
        .toLowerCase();

    let termos = document.getElementsByTagName("dt");

    let encontrou = false;

    for (let i = 0; i < termos.length; i++) {

        let textoTermo = termos[i].innerText.toLowerCase();

        if (textoTermo.includes(termoPesquisa)) {

            // acha a letra (pai da div)
            let divLetra = termos[i].closest("div");
            let idLetra = divLetra.id;

            let conteudo = document.getElementById(idLetra).innerHTML;

            let card = document.getElementById("letraselecionada");

            card.innerHTML = conteudo;
            card.style.display = "block";

            encontrou = true;
            break;
        }
    }

    if (!encontrou) {
        alert("Termo não encontrado no glossário.");
    }
}