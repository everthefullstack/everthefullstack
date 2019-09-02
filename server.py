# coding=UTF-8
from flask import Flask, render_template, render_template_string
from flask_sslify import SSLify

# instancia o app
app = Flask(__name__)
sslify = SSLify(app)
app.config.from_object('config.ProductionConfig')

############################################################################################################################################
# inicia o site
@app.route('/')
def index():

    return render_template("index.html")
############################################################################################################################################
@app.route('/skills')
def skills():

    return render_template('skills.html')
############################################################################################################################################
@app.route('/formacao')
def formacao():

    template = """<h1>Página formação em construção</h1> <br> <a href="{{ url_for('index') }}">Voltar para o início</a>"""
    return render_template_string(template)
############################################################################################################################################
@app.route('/experiencia')
def experiencia():

    template = """<h1>Página experiência em construção</h1> <br> <a href="{{ url_for('index') }}">Voltar para o início</a>"""
    return render_template_string(template)
############################################################################################################################################
@app.route('/sobre')
def sobre():

    template = """<h1>Página sobre em construção</h1> <br> <a href="{{ url_for('index') }}">Voltar para o início</a>"""
    return render_template_string(template)
############################################################################################################################################
@app.route('/blog')
def blog():

    template = """<h1>Página blog em construção</h1> <br> <a href="{{ url_for('index') }}">Voltar para o início</a>"""
    return render_template_string(template)
############################################################################################################################################
# inicia o servidor
if __name__ == "__main__":
    app.run()


