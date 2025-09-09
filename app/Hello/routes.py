from flask import Blueprint, render_template, request, Response, redirect, url_for
from ..models import User, db

hello_bp = Blueprint('Hello', __name__)
name_bp = Blueprint('HelloNome', __name__)

@hello_bp.route('/')
def index():
    usuarios = User.query.all()
    return render_template('index.html', usuarios=usuarios)


# @name_bp.route('/sobre')
# def index():
#     return render_template('sobre.html')

@hello_bp.route('/novoUsuario', methods=['POST'])
def novo_usuario():
    nome_usuario = request.form['nome_usuario']

    novo_user = User(username = nome_usuario)
    db.session.add(novo_user)
    db.session.commit()
    return redirect('/')

@hello_bp.route('/deletarUsuario/<int:usuario_id>', methods=['POST'])
def deletar_usuario(usuario_id):
    usuario = User.query.get(usuario_id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
    return redirect(url_for('Hello.index'))

@hello_bp.route('/editarUsuario/<int:usuario_id>', methods=['POST'])
def editar_usuario(usuario_id):
    usuario = User.query.get(usuario_id)
    if usuario:
        usuario.username = request.form['nome_usuario']
        db.session.commit()
    return redirect(url_for('Hello.index'))