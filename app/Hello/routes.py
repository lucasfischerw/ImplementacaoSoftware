from flask import Blueprint

hello_bp = Blueprint('Hello', __name__)
name_bp = Blueprint('HelloNome', __name__)

@hello_bp.route('/')
def index():
    return "<div style='display:grid;place-content:center;background-color:orange;color:white;width: 100vw;height:100vh;'><h1 style='font-weight:bold;text-align:center;'>Olá mundo!</h1></br><a href='/sobre' style='background-color: white;padding: 10px;color:black;border-radius: 15px;text-align-center;'>Acessar página sobre</a>"

@name_bp.route('/sobre')
def index():
    return "<div style='display:grid;place-content:center;background-color:red;color:white;width: 100vw;height:100vh;'><h1 style='font-weight:bold;text-align:center;'>Olá, Lucas Fischer!</h1></br><a style='background-color: white;padding: 10px;color:black;border-radius: 15px; text-align-center;' href='/'>Voltar à página inicial</a>"