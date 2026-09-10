function verificarFormulario() {

    let senha = document.getElementById("senha");

    if (senha.value.length < 8) {

        alert(
            "Senha incorreta.\n\n" +
            "A senha precisa possuir pelo menos 8 caracteres."
        );

        return false;
    }

    return true;
}