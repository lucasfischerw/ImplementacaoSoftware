from flask import Blueprint, render_template
from ..models import User, db

hello_bp = Blueprint('Hello', __name__)
name_bp = Blueprint('HelloNome', __name__)

@hello_bp.route('/')
def index():
    usuarios = User.query.all()
    return render_template('index.html', usuarios=usuarios)


@name_bp.route('/sobre')
def index():
    return render_template('sobre.html')