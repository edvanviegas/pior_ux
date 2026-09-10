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
        senha = request.form.get("senha")

        if not nome or not email or not senha:
            return render_template(
                "cadastro.html",
                erro="Erro: todos os campos opcionais são obrigatórios."
            )

        if len(senha) < 8:
            return render_template(
                "cadastro.html",
                erro="Senha inválida. A senha precisa ter pelo menos 8 caracteres."
            )

        return redirect(url_for("final"))

    return render_template("cadastro.html")


@app.route("/final")
def final():
    return render_template("final.html")


if __name__ == "__main__":
    app.run(debug=True)