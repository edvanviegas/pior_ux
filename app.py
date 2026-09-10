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
        if not senha:
            erros.append("A senha não pode ficar vazia.")

        else:

            if len(senha) < 12:
                erros.append(
                    "A senha precisa possuir pelo menos 12 caracteres."
                )

            if not any(c.isupper() for c in senha):
                erros.append(
                    "A senha precisa possuir uma letra maiúscula."
                )

            if not any(c.islower() for c in senha):
                erros.append(
                    "A senha precisa possuir uma letra minúscula."
                )

            if not any(c.isdigit() for c in senha):
                erros.append(
                    "A senha precisa possuir um número."
                )

            if not any(c in "!@#$%&*?" for c in senha):
                erros.append(
                    "A senha precisa possuir um símbolo especial."
                )

            if " " in senha:
                erros.append(
                    "A senha não pode possuir espaços."
                )

            if senha.lower() == senha:
                erros.append(
                    "A senha precisa demonstrar maior diversidade."
                )

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