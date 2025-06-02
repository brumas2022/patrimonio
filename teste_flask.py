from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'PAGINA INICIAL'

@app.route('/beatles')
def musica():
    return 'AQUI SO TEREMOS BEATLES'

app.run()


