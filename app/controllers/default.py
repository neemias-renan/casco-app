from app import app, db
from flask import render_template,redirect,url_for,request
# from flask_login import login_user
# from flask_login import login_required, current_user

from app.models.tables import Lider,Pesquisador
from app.models.forms import LoginForm,CadastroLiderForm,CadastroPesquisadorForm

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods = ["GET","POST"])
def login():
    form = LoginForm()
    # if form.validate_on_submit():
    #     lider = Lider.query.filter_by(email = form.email.data).first()
    #     if lider and lider.senha == form.senha.data:
    #         login_user(lider)
    #         print("Bem vindo.")
    #     else:
    #         print("Dados Inválidos.")

    return render_template('login.html',form = form)

@app.route("/inscreverse", methods = ["GET","POST"])
def inscreverse():
    form = CadastroPesquisadorForm()
    if form.validate_on_submit():
        if form.senha.data == form.confirmarSenha.data:
            if request.method == 'POST':
                pesquisador = Pesquisador(form.nome.data, form.email.data, form.senha.data)
                db.session.add(pesquisador)
                db.session.commit()
                return redirect(url_for('login'))
        else:
            # MELHORAR ISSO
            print("corrija a senha")
    return render_template('cadastroP.html',form = form)

@app.route("/inscrevase", methods = ["GET","POST"])
def inscrevase():
    form = CadastroLiderForm()
    if form.validate_on_submit():
        if form.senha.data == form.confirmarSenha.data:
            if request.method == 'POST':
                lider = Lider(form.nome.data, form.email.data, form.senha.data)
                db.session.add(lider)
                db.session.commit()
                return redirect(url_for('login'))
        else:
            # MELHORAR ISSO
            print("corrija a senha")

    return render_template('cadastroL.html',form = form)

@app.route("/teste/<info>")
@app.route("/teste",defaults = {"info":None})
def teste(info):
    i = Lider('Neemias',"ee@g.com","123")
    db.session.add(i)
    db.session.commit()
    return "ok"
