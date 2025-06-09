from flask import Flask, jsonify, request

app = Flask(__name__)

agenda  = [
    {
        'id': 1,
        'nome': "marcos",
        'telefone': "66999945695"
    }, 
    {
        'id': 2,
        'nome': "mara",
        'telefone': "66996419429"
    }, 
    {
        'id': 3,
        'nome': "faisca",
        'telefone': "66992097580"
    }
]
@app.route('/')
def pagina():
    return "SEBO DO MARCAO"
@app.route('/agenda')
def obter_agenda():
    return jsonify(agenda)

app.run(port=5000, host='localhost', debug=True)