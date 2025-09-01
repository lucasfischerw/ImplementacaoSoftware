from flask import Blueprint

hello_bp = Blueprint('Hello', __name__)

@hello_bp.route('/')
def index():
    return "<div style='display:grid;place-content:center;background-color:red;color:white;'><h1 style='font-weight:bold;text-align:center;'>Aprendendo FLASK :)</h1></br><img width='500' height='300' style='margin:auto;text-align:center;' src='https://revistaanamaria.com.br/wp-content/uploads/2025/01/Voce-sabe-identificar-se-seu-cachorro-esta-triste-ou-feliz_-Aprenda-750x375.jpg'></br><h1 style='text-align:center;'>CACHORRO FELIZ!!</h1>"