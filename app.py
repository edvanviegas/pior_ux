from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "chave-do-projeto-pior-ux"


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

        if not nome:
            erros.append("O nome aparentemente decidiu não existir.")

        if not email:
            erros.append("O endereço eletrônico é obrigatório.")

        if not idade:
            erros.append("Precisamos saber sua idade.")

        if not cidade:
            erros.append("A cidade é obrigatória.")

        # SENHA MAIS DIFÍCIL
        if not senha:
            erros.append("A senha está vazia. Isso parece uma péssima ideia.")

        else:
            if len(senha) < 10:
                erros.append("A senha precisa ter pelo menos 10 caracteres.")

            if not any(c.isupper() for c in senha):
                erros.append("A senha precisa ter uma letra MAIÚSCULA.")

            if not any(c.islower() for c in senha):
                erros.append("A senha precisa ter uma letra minúscula.")

            if not any(c.isdigit() for c in senha):
                erros.append("A senha precisa ter pelo menos um número.")

            if not any(c in "!@#$%&*" for c in senha):
                erros.append(
                    "A senha precisa ter um caractere especial: ! @ # $ % & *"
                )

        if erros:
            return render_template(
                "cadastro.html",
                erros=erros,
                nome=nome,
                email=email,
                idade=idade,
                cidade=cidade
            )

        # Guardamos os dados temporariamente para a confirmação
        session["cadastro"] = {
            "nome": nome,
            "email": email,
            "idade": idade,
            "cidade": cidade
        }

        return redirect(url_for("confirmacao"))

    return render_template("cadastro.html", erros=[])


@app.route("/confirmacao", methods=["GET", "POST"])
def confirmacao():

    cadastro = session.get("cadastro")

    if not cadastro:
        return redirect(url_for("cadastro"))

    if request.method == "POST":
        return redirect(url_for("final"))

    return render_template(
        "confirmacao.html",
        cadastro=cadastro
    )


@app.route("/final")
def final():
    return render_template("final.html")


if __name__ == "__main__":
    app.run(debug=True)