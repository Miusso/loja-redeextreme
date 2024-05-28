from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def homepage():

    return render_template("homepage.html")

@app.route("/servicos")
def servicos():
    return render_template("servicos.html")

@app.route("/Area_do_cliente/<nome_usuario>")
def usuario(nome_usuario):
    return render_template("Area_do_cliente.html", nome_usuario=nome_usuario)

if __name__ == "__main__":
    app.run(debug=True)