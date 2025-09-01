from flask import *
from .Hello.routes import hello_bp, name_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(hello_bp)
    app.register_blueprint(name_bp)
    
    return app