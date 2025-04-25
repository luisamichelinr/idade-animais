from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def cachorro(idade):
    if idade == 1:
        idade_hum = 15
    elif idade == 2:
        idade_hum = 24
    else:
        idade_hum = 24 + (idade - 2) * 5

    return idade_hum

def gato(idade):
    if idade == 1:
        idade_hum = 15
    elif idade == 2:
        idade_hum = 24
    else:
        idade_hum = 24 + (idade - 2) * 4
    return idade_hum
@app.route('/calcular_idade', methods=['POST'])
def calcular_idade():
    try:
        tipo = str(request.form['tipo'] )
        anos = int(request.form['anos'])

        if tipo == "1":
            idade_hum = cachorro(anos)

        elif tipo == "2":
            idade_hum = gato(anos)

        return render_template('index.html', idade_hum=idade_hum)

    except Exception as e:
        idade_hum = f"Ocorreu um erro inesperado {e}"
        return render_template('index.html', idade_hum=idade_hum)

if __name__ == '__main__':
    app.run(debug=True)