from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'PAGINA INICIAL'

app.run()


