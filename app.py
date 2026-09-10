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

        if not nome:
            erros.append("O nome aparentemente decidiu não existir.")

        if not email:
            erros.append("O endereço eletrônico é obrigatório, provavelmente.")

        if not idade:
            erros.append("Precisamos saber sua idade para continuar.")

        if not senha:
            erros.append("A senha está vazia. Isso parece inseguro.")

        if len(senha) < 8:
            erros.append("A senha precisa ter pelo menos 8 caracteres.")

        if not cidade:
            erros.append("A cidade é obrigatória porque o formulário decidiu.")

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

    return render_template("cadastro.html", erros=[])


@app.route("/confirmacao", methods=["GET", "POST"])
def confirmacao():

    if request.method == "POST":
        return redirect(url_for("final"))

    return render_template("confirmacao.html")


@app.route("/final")
def final():
    return render_template("final.html")


if __name__ == "__main__":
    app.run(debug=True)