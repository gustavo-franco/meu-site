from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", title="Gustavo Franco")

@app.route("/projects")
def projects():
    return render_template("projects.html", title="Projetos")

@app.route("/projects/crypto-news")
def project_crypto():
    return render_template("project_crypto.html", title="Agregador de Notícias Cripto")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
