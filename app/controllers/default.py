from flask import render_template,redirect,url_for,request
from flask_login import login_user,logout_user,current_user,login_required
from app import app, db , lm
from datetime import date,timedelta
from app.controllers.functions import *

from app.models.tables import Equipe, User, Tartaruga,Nova_Desova
from app.models.forms import LoginForm,CadastroLiderForm,CadastroPesquisadorForm, CadastroEquipeForm
from operator import itemgetter, attrgetter

import random
import string

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id = id).first()

@app.route("/index", methods = ["GET","POST"])
@app.route("/", methods = ["GET","POST"])
def index():
    form = LoginForm()
    alerta_erro = ""
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email = form.email.data).first()
            if user.email == None:
                alerta_erro = "Há algo de errado em seus dados."
    
            if user and user.senha == form.senha.data:
                login_user(user)
                return redirect(url_for('inicio'))
            else:
                alerta_erro = "Há algo de errado em seus dados."
        except:
            alerta_erro = "Há algo de errado em seus dados."
    return render_template('login.html',form = form,alerta_erro = alerta_erro)


@app.route("/inicio" , methods = ["GET", "POST"])
@login_required
def inicio():
    alertasdeTartarugas = ''
    alertasdeDesova = ''

    primeiroNome = exibirNomedoUsuario(current_user.nome) 
    nome_equipe = exibirNomedaEquipe(current_user.equipe_id)

    if nome_equipe == None:
        equipe = ""
        codigo = ""
    else:
        if current_user.tipo == "pesquisador":
            equipe =  nome_equipe.nomedaequipe
            codigo = ""
        else:
            equipe = nome_equipe.nomedaequipe
            codigo = "Código de acesso: "+nome_equipe.codigodaequipe
    # A data atual vai fazer exibir as notificações das desovas
    dataAtual = exibirDatadeHoje()

    # -- Pensar como continuar a exibir esse alerta mesmo depois do dia
    alertasdeTartarugas = Tartaruga.query.filter_by(datadoalerta = dataAtual).all()
    alertasdeDesova = Nova_Desova.query.filter_by(datadoalerta = dataAtual).all()
    return render_template('inicio.html',alertasdeTartarugas = alertasdeTartarugas, alertasdeDesova = alertasdeDesova,equipe = equipe,codigo=codigo, primeiroNome = primeiroNome)


@app.route("/editarperfil",methods=["GET","POST"])
@login_required
def editarperfil():
    user = User.query.filter_by(id = current_user.id).first()
    alerta_erro = ''
    if request.method == 'POST':
        user.nome = request.form["novoNome"]
        user.email = request.form["novoEmail"]

        if request.form['senhaAtual'] == user.senha:
            user.senha = request.form["senhaNova"]
            db.session.commit()
            print("Foi atualizado.")
        elif request.form['senhaAtual'] == '':
            alerta_erro = ""
            print('está vazio')
        else:
            alerta_erro = "As senhas não coincidem"
            print('erro')
        

    return render_template('editarperfil.html',alerta_erro = alerta_erro)


@app.route("/gerenciarequipe",methods=["GET","POST"])
@login_required
def gerenciarequipe():
    membros = ""
    equipe_nome = ""
    lider_nome = ""


    nomedaEquipe = exibirNomedaEquipe(current_user.equipe_id)
    equipe_nome = nomedaEquipe.nomedaequipe

    lider_nome = exibirNomedoLiderdaEquipe(current_user.equipe_id)
    todosMembrosdaEquipe = exibirMembrosdaEquipe(current_user.equipe_id)  

    del todosMembrosdaEquipe[0]
    membros = todosMembrosdaEquipe

    if request.method == 'POST':
        nomedaEquipe.nomedaequipe = request.form['novoNomedaEquipe']
        db.session.commit()
        return redirect(url_for('gerenciarequipe'))

    return render_template('gerenciarequipe.html',membros = membros, equipe_nome = equipe_nome,lider_nome = lider_nome)

@app.route("/historico", methods = ["GET","POST"])
@login_required
def historico():
    tartarugas_dados = ''
    alerta_erro = ''
    usuario = current_user.tipo
    if request.method == 'POST':
        identificador = request.form['identificador']
        buscar_anilha = Tartaruga.query.filter_by(anilha = identificador).all()

        ordenarAnilhas = sorted(buscar_anilha,key=attrgetter('data'))
        if buscar_anilha == []:
            alerta_erro = "A anilha procurada não foi achada."
            todos = Tartaruga.query.all()
            ordenarTodos1 = sorted(todos,key=attrgetter('data'))
            tartarugas_dados = ordenarTodos1
        else:
            tartarugas_dados = ordenarAnilhas

    else:
        todos = Tartaruga.query.all()
        ordenarTodos2 = sorted(todos,key=attrgetter('data'))
        tartarugas_dados = ordenarTodos2
        print("tá aqui")
    return render_template('historico.html', t = tartarugas_dados, alerta_erro = alerta_erro, usuario = usuario)


@app.route("/registrarTartaruga",methods = ["GET","POST"])
@login_required
def registrarTartaruga():
    alerta_erro = ""
    if request.method == 'POST':
        try:
            anilha = request.form['numerodaanilha']
            informacoes = request.form['informacoes']
            especie = request.form['especie']
            tipo_de_registro = request.form['tipodeRegistro']
            sexo = request.form['sexo']
            ccc = request.form['ccc']
            lcc = request.form['lcc']
            municipio = request.form['municipio']
            praia = request.form['praia']
            latitude = request.form['latitude']
            longitude = request.form['longitude']
            hora = request.form['hora']
            data = request.form['data']

            dataOriginal = realizarCorrecaodeDataOriginal(data)
            datadoFuturoAlerta = realizarCorrecaodeDatadeFuturoAlerta(data)
    
            tartaruga = Tartaruga(anilha,informacoes,especie,tipo_de_registro,sexo,ccc,lcc,municipio,praia,latitude,longitude,dataOriginal,hora,datadoFuturoAlerta)

            db.session.add(tartaruga)
            db.session.commit()
            return redirect(url_for('inicio'))
        except:
            alerta_erro = "Há dados faltando, insira novamente."
    return render_template("registrarTartaruga.html", alerta_erro = alerta_erro)


@app.route("/novaEclosao" , methods = ["GET", "POST"])
@login_required
def novaeclosao():
    alerta_erro = ""
    if request.method == 'POST':
        try:
            municipio = request.form['municipio']
            praia = request.form['praia']
            latitude = request.form['latitude']
            longitude = request.form['longitude']
            hora = request.form['hora']
            data = request.form['data']
            
            dataOriginal = realizarCorrecaodeDataOriginal(data)
            datadoFuturoAlerta = realizarCorrecaodeDatadeFuturoAlerta(data)

            novadesova = Nova_Desova(municipio,praia,latitude,longitude,dataOriginal,hora,datadoFuturoAlerta)
            db.session.add(novadesova)
            db.session.commit()
            return redirect(url_for('principal'))
        except:
            alerta_erro = "Há dados faltando, insira novamente."
    return render_template("novaeclosao.html", alerta_erro = alerta_erro)


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/registrarpesquisador", methods = ["GET","POST"])
def registrarPesquisador():
    form = CadastroPesquisadorForm()
    alerta_email = ""
    alerta_senha = ""
    alerta_codigo = ""
    if form.validate_on_submit():
        if form.senha.data == form.confirmarSenha.data:
            if request.method == 'POST':
                codigoInput = Equipe.query.filter_by(codigodaequipe=form.codigoequipe.data).first()
                if codigoInput == None:
                    alerta_codigo = "Código da equipe não existe"
                else:
                    try:
                        email = User.query.filter_by(email=form.email.data).first()
                        if email.email == form.email.data:
                            alerta_email = "o email adicionado já existe."
                    except AttributeError:
                        pesquisador = User(form.nome.data, form.email.data, form.senha.data,'pesquisador',equipes='')
                        db.session.add(pesquisador)
                        teste = User.query.filter_by(email = form.email.data).first()
                        teste.equipe_id = codigoInput.id
                        db.session.commit()
                        return redirect(url_for('index'))
        else:
            alerta_senha = "As senhas não coincidem"
    return render_template('cadastroP.html',form = form, alerta_senha = alerta_senha, alerta_email = alerta_email,alerta_codigo=alerta_codigo)


@app.route("/registrarlider", methods = ["GET","POST"])
def registrarLider():
    form = CadastroLiderForm()
    alerta_email = ""
    alerta_senha = ""
    alerta_equipe = ""
    letras = string.ascii_uppercase

    equipeform = CadastroEquipeForm()
    
    if form.validate_on_submit():
        if form.senha.data == form.confirmarSenha.data:
            if request.method == 'POST':
                codigo = ''.join(random.choice(letras) for _ in range(10))                
                equipe = Equipe(equipeform.nomedaequipe.data,codigo)
                lider = User(form.nome.data, form.email.data, form.senha.data,'lider',equipes=equipe)
                try:
                    email = User.query.filter_by(email=form.email.data).first()
                    NomeDaEquipe = Equipe.query.filter_by(nomedaequipe= equipe.nomedaequipe).first()

                    if email.email == form.email.data:
                        alerta_email = "o email adicionado já existe."
                    if NomeDaEquipe.nomedaequipe == equipeform.nomedaequipe.data:
                        alerta_equipe = "Esse nome já está em uso"
                except AttributeError:
                    db.session.add(lider)
                    db.session.add(equipe)
                    db.session.commit()
                    return redirect(url_for('index'))               
        else:
            alerta_senha = "As senhas não coincidem"
    return render_template('cadastroL.html',form = form, equipeform = equipeform, alerta_senha = alerta_senha, alerta_email = alerta_email,alerta_equipe = alerta_equipe)


@app.route("/recuperarsenha",methods=["GET","POST"])
def recuperarsenha():
    return render_template('recuperarsenha.html')



@app.route("/apagar_tartaruga/<id>")
@login_required
def apagar_tartaruga(id):
    tartaruga = Tartaruga.query.filter_by(id = id).first()
    db.session.delete(tartaruga)
    db.session.commit()
    return redirect(url_for('historico'))  


@app.route("/apagar_user/<id>")
@login_required
def apagar_user(id):
    user = User.query.filter_by(id = id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('gerenciarequipe')) 

@app.errorhandler(404)
def not_found_error(error):
    return  redirect(url_for('index')), 404

@lm.unauthorized_handler
def unauthorized():
    return redirect(url_for('index'))