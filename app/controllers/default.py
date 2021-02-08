from flask import render_template,redirect,url_for,request
from flask_login import login_user,logout_user,current_user
from app import app, db , lm
from datetime import date,timedelta
# from flask.login import 

# from flask_login import login_required, current_user

from app.models.tables import Equipe, User, Tartaruga,Nova_Desova
from app.models.forms import LoginForm,CadastroLiderForm,CadastroPesquisadorForm, CadastroEquipeForm

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id = id).first()

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods = ["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and user.senha == form.senha.data:
                login_user(user)
                return redirect(url_for('principal'))
                return "ok"
        else:
            print("falhou,")
    
    #             print("Bem vindo.")
    #         if not l or l.verify_password():
    #             print("Dados Inválidos.")
    return render_template('login.html',form = form)

@app.route("/principal" , methods = ["GET", "POST"])
def principal():
    if request.method == 'POST':
        anilha = request.form['numerodaanilha']
        informacoes = request.form['informacoes']
        especie = request.form['especie']
        tipo_de_registro = request.form['tipodeRegistro']
        monitoramento = request.form['monitoramento']
        sexo = request.form['sexo']
        ccc = request.form['ccc']
        lcc = request.form['lcc']

        municipio = request.form['municipio']
        praia = request.form['praia']
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        
        hora = request.form['hora']
        dataOriginal = request.form['data']

        # separei a data original
        data1 = dataOriginal.split("-")
        
        ano1 = int(data1[0])
        mes1 = int(data1[1])
        dia1 = int(data1[2])

        # juntei a Data Original
        data = str("%s/%s/%s" %(dia1,mes1, ano1))
        # peguei cada item e coloquei dentro do "date"
        novadata = date(ano1,mes1,dia1)
        # adicionei mais dias, para fazer a comparação futuramente
        novadata2 = str(novadata + timedelta(days = 2))
        # ******************************LEMBRAR DE TROCAR PARA 45 DIAS*****
        # separei a novadata2
        data2 = novadata2.split("-")
        ano2 = int(data2[0])
        mes2 = int(data2[1])
        dia2 = int(data2[2])

        datadoalerta = str("%s/%s/%s"%(dia2,mes2,ano2))

        tartaruga = Tartaruga(anilha,informacoes,especie,tipo_de_registro,monitoramento,sexo,ccc,lcc,municipio,praia,latitude,longitude,data,hora,datadoalerta)
        db.session.add(tartaruga)
        db.session.commit()
        
        return redirect(url_for('principal'))

# **********************************************
    a = ''
    hoje = str(date.today())
    novoHoje = hoje.split("-")
    ano3 = int(novoHoje[0])
    mes3 = int(novoHoje[1])
    dia3 = int(novoHoje[2])

    diaatual = str("%r/%r/%r" %(dia3,mes3,ano3))
    print(diaatual)
    
    alertas = Tartaruga.query.filter_by(datadoalerta <= diaatual).all()
    a = alertas
    
    return render_template("init.html",a = a)

@app.route("/novadesova" , methods = ["GET", "POST"])
def novadesova():
    if request.method == 'POST':
        municipio = request.form['municipio']
        praia = request.form['praia']
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        data = request.form['data']
        hora = request.form['hora']
        monitoramento = request.form['monitoramento']
                # *****        

        novadesova = Nova_Desova(municipio,praia,latitude,longitude,data,hora,monitoramento)
        db.session.add(novadesova)
        db.session.commit()
        return redirect(url_for('principal'))
    return render_template("novadesova.html")

@app.route("/historico", methods = ["GET","POST"])
def historico():
    t = ''
    if request.method == 'POST':
        identificador = request.form['identificador']


        todos = Tartaruga.query.filter_by(anilha = identificador).all()
        print(todos)
        t = todos
        


    return render_template('historico.html', t = t)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))



# Registrar Pesquisador
@app.route("/registerp", methods = ["GET","POST"])
def registerp():
    form = CadastroPesquisadorForm()
    if form.validate_on_submit():
        if form.senha.data == form.confirmarSenha.data:
            if request.method == 'POST':
                pesquisador = User(form.nome.data, form.email.data, form.senha.data,'pesquisador')
                db.session.add(pesquisador)
                db.session.commit()
                return redirect(url_for('login'))
        else:
            # MELHORAR ISSO
            print("corrija a senha")
    return render_template('cadastroP.html',form = form)

# Registrar Lider
@app.route("/registerl", methods = ["GET","POST"])
def registerL():
    form = CadastroLiderForm()
    equipeform = CadastroEquipeForm()
    
    if form.validate_on_submit():
        if form.senha.data == form.confirmarSenha.data:
            if request.method == 'POST':
                lider = User(form.nome.data, form.email.data, form.senha.data,'lider')
                equipe = Equipe(equipeform.nomedaequipe.data)

                db.session.add(lider)
                db.session.add(equipe)

                db.session.commit()
                return redirect(url_for('login'))
        else:
            # MELHORAR ISSO
            print("corrija a senha")

    return render_template('cadastroL.html',form = form, equipeform = equipeform)


@app.route("/configuracoes",methods=["GET","POST"])
def configuracoes():
    #     identificador = request.form['identificador']
    user = User.query.filter_by(id = current_user.id).first()

    if request.method == 'POST':
        user.nome = request.form["novoNome"]
        user.email = request.form["novoEmail"]

        if request.form['senhaAtual'] == user.senha:
            user.senha = request.form["senhaNova"]
        db.session.commit()
        print("ok")
        

    return render_template('configuracoes.html')


@app.route("/recuperarsenha",methods=["GET","POST"])
def recuperarsenha():
    return render_template('recuperarsenha.html')



@app.route("/teste/<info>")
@app.route("/teste",defaults = {"info":None})
def teste(info):
    i = Tartaruga.query.filter_by(id="1").first()
    db.session.delete(i)
    db.session.commit()
    return "ok"
