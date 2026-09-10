from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":

        nome = request.form.get("nome")
        email = request.form.get("email")
        idade = request.form.get("idade")
        senha = request.form.get("senha")
        cidade = request.form.get("cidade")

        erros = []

        # Nome
        if not nome:
            erros.append("O campo Nome parece estar vazio.")

        elif len(nome) < 3:
            erros.append("O nome precisa ter pelo menos 3 caracteres.")

        # E-mail
        if not email:
            erros.append("O campo E-mail é obrigatório.")

        elif "@" not in email:
            erros.append("O e-mail precisa possuir um @.")

        # Idade
        if not idade:
            erros.append("A idade é necessária para continuar.")

        else:
            try:
                idade_numero = int(idade)

                if idade_numero < 13:
                    erros.append(
                        "A idade informada não parece ser compatível."
                    )

                if idade_numero > 120:
                    erros.append(
                        "A idade informada parece um pouco exagerada."
                    )

            except ValueError:
                erros.append("A idade precisa ser um número.")

        # Cidade
        if not cidade:
            erros.append("Você esqueceu de selecionar sua cidade.")

        # SENHA DIFÍCIL
        # SENHA ABSURDAMENTE DIFÍCIL
if not senha:
    erros.append("A senha é obrigatória.")

else:
    if len(senha) < 16:
        erros.append("A senha precisa ter pelo menos 16 caracteres.")

    if len(senha) > 30:
        erros.append("A senha não pode ter mais de 30 caracteres.")

    if not any(c.isupper() for c in senha):
        erros.append("A senha precisa ter pelo menos 1 letra MAIÚSCULA.")

    if not any(c.islower() for c in senha):
        erros.append("A senha precisa ter pelo menos 1 letra minúscula.")

    if not any(c.isdigit() for c in senha):
        erros.append("A senha precisa ter pelo menos 1 número.")

    if not any(c in "!@#$%&*?" for c in senha):
        erros.append("A senha precisa ter pelo menos 1 símbolo especial.")

    if " " in senha:
        erros.append("A senha não pode possuir espaços.")

    if any(c in senha for c in "áéíóúãõâêôç"):
        erros.append("A senha não pode possuir caracteres acentuados.")

    if senha[0].isdigit():
        erros.append("A senha não pode começar com número.")

    if senha[-1].isdigit():
        erros.append("A senha não pode terminar com número.")

    if senha.lower().startswith("senha"):
        erros.append("A senha não pode começar com a palavra 'senha'.")

    if senha.lower() == senha:
        erros.append("A senha precisa possuir letras maiúsculas.")

    if senha.upper() == senha:
        erros.append("A senha precisa possuir letras minúsculas.")

    # Precisa ter pelo menos 2 números
    if sum(c.isdigit() for c in senha) < 2:
        erros.append("A senha precisa possuir pelo menos 2 números.")

    # Precisa ter pelo menos 2 símbolos
    if sum(c in "!@#$%&*?" for c in senha) < 2:
        erros.append("A senha precisa possuir pelo menos 2 símbolos especiais.")

    # Não pode repetir o mesmo caractere 3 vezes seguidas
    if any(senha[i] == senha[i+1] == senha[i+2]
           for i in range(len(senha) - 2)):
        erros.append("A senha não pode repetir o mesmo caractere 3 vezes seguidas.")

    # Não pode conter sequências óbvias
    sequencias = [
        "123", "234", "345", "456", "567",
        "678", "789", "abc", "bcd", "cde",
        "qwe", "asd", "zxc"
    ]

    if any(seq in senha.lower() for seq in sequencias):
        erros.append("A senha não pode conter sequências óbvias.")

    # Precisa ter pelo menos 4 caracteres diferentes de letras
    caracteres_especiais = sum(
        not c.isalnum() for c in senha
    )

    if caracteres_especiais < 2:
        erros.append("A senha precisa possuir pelo menos 2 caracteres especiais.")

        # Se houver erros, volta para o formulário
        if erros:

            return render_template(
                "cadastro.html",
                erros=erros,
                nome=nome,
                email=email,
                idade=idade,
                cidade=cidade
            )

        return redirect(url_for("confirmacao"))


    return render_template(
        "cadastro.html",
        erros=[]
    )


@app.route("/confirmacao", methods=["GET", "POST"])
def confirmacao():

    if request.method == "POST":

        confirmado = request.form.get("confirmado")

        if confirmado:

            return redirect(url_for("final"))

        return render_template(
            "confirmacao.html",
            erro="Você precisa confirmar que não sabe exatamente o que confirmou."
        )

    return render_template(
        "confirmacao.html",
        erro=None
    )


@app.route("/final")
def final():

    return render_template("final.html")


if __name__ == "__main__":
    app.run(debug=True)