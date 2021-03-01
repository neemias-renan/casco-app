from flask import render_template,redirect,url_for,request
from flask_login import login_user,logout_user,current_user,login_required
from app import app, db , lm
from datetime import date,timedelta


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
                print("erro lugar 1")
    
            if user and user.senha == form.senha.data:
                login_user(user)
                return redirect(url_for('inicio'))
            else:
                alerta_erro = "Há algo de errado em seus dados."
                print("erro lugar 2")
        except:
            alerta_erro = "Há algo de errado em seus dados."
            print("aqui é o erro")
    return render_template('login.html',form = form,alerta_erro = alerta_erro)


@app.route("/inicio" , methods = ["GET", "POST"])
@login_required
def inicio():
    # **********************************************
    a = ''
    d = ''
    id_equipe = current_user.equipe_id
    nome_equipe = Equipe.query.filter_by(id = id_equipe).first()
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
    hoje = str(date.today())
    novoHoje = hoje.split("-")
    ano3 = int(novoHoje[0])
    mes3 = int(novoHoje[1])
    dia3 = int(novoHoje[2])
    diaatual = str("%r/%r/%r" %('%02d' % dia3,'%02d' % mes3, ano3))
    eliminar = "'"
    for i in range(0,len(eliminar)):
        diaatual = diaatual.replace(diaatual[i],"")
    # Pensar como continuar a exibir esse alerta mesmo depois do dia
    alertas = Tartaruga.query.filter_by(datadoalerta = diaatual).all()
    alertas2 = Nova_Desova.query.filter_by(datadoalerta = diaatual).all()
    a = alertas
    d = alertas2
    return render_template('inicio.html',a = a, d = d,equipe = equipe,codigo=codigo)


@app.route("/editarperfil",methods=["GET","POST"])
@login_required
def editarperfil():
    #     identificador = request.form['identificador']
    user = User.query.filter_by(id = current_user.id).first()

    if request.method == 'POST':
        user.nome = request.form["novoNome"]
        user.email = request.form["novoEmail"]

        if request.form['senhaAtual'] == user.senha:
            user.senha = request.form["senhaNova"]
        db.session.commit()
        print("ok")
        

    return render_template('editarperfil.html')


@app.route("/gerenciarequipe")
@login_required
def gerenciarequipe():
    membros = ""
    equipe_nome = ""
    lider_nome = ""
    id_equipe = current_user.equipe_id
    nome_equipe = Equipe.query.filter_by(id = id_equipe).first()

    

    lider = User.query.filter_by(equipe_id = id_equipe).first()
    lider_nome = lider.nome

    todaequipe = User.query.filter_by(equipe_id = id_equipe).all()   
    equipe_nome = nome_equipe.nomedaequipe
    del todaequipe[0]
    membros = todaequipe


    return render_template('gerenciarequipe.html',membros = membros, equipe_nome = equipe_nome,lider_nome = lider_nome)

@app.route("/historico", methods = ["GET","POST"])
@login_required
def historico():
    t = ''
    g = ''
    if request.method == 'POST':
        identificador = request.form['identificador']
        busca = Tartaruga.query.filter_by(anilha = identificador).all()

        ordenar = sorted(busca,key=attrgetter('data'), reverse=True)
        if busca == []:
            todos = Tartaruga.query.all()
            ordenarTodos = sorted(todos,key=attrgetter('data'), reverse=True)
            g = ordenarTodos
        else:
            t = ordenar
            g = ''
    else:
        todos = Tartaruga.query.all()
        ordenarTodos = sorted(todos,key=attrgetter('data'), reverse=True)
        g = ordenarTodos
    return render_template('historico.html', t = t, g = g)


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
            dataOriginal = request.form['data']

            # separei a data original
            data1 = dataOriginal.split("-")
            
            ano1 = int(data1[0])
            mes1 = int(data1[1])
            dia1 = int(data1[2])

            # juntei a Data Original
            data = str("%s/%s/%s" %('%02d' % dia1,'%02d' % mes1,'%02d' % ano1))
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

            datadoalerta = str("%s/%s/%s"%('%02d' %dia2,'%02d' %mes2,'%02d' %ano2))

            tartaruga = Tartaruga(anilha,informacoes,especie,tipo_de_registro,sexo,ccc,lcc,municipio,praia,latitude,longitude,data,hora,datadoalerta)
            db.session.add(tartaruga)
            db.session.commit()
            return redirect(url_for('inicio'))
        except:
            alerta_erro = "Há dados faltando, insira novamente."
    return render_template("registrarTartaruga.html",alerta_erro = alerta_erro)


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
                    # *****
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

            novadesova = Nova_Desova(municipio,praia,latitude,longitude,data,hora,datadoalerta)
            db.session.add(novadesova)
            db.session.commit()
            return redirect(url_for('principal'))
        except:
            alerta_erro = "Há dados faltando, insira novamente."
    return render_template("novaeclosao.html",alerta_erro = alerta_erro)


@app.route("/sobre")
@login_required
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
                        # Aqui não está sendo passado o id da equipe, FUTURAMENTE será resolvido.
                        db.session.add(pesquisador)
                        teste = User.query.filter_by(email = form.email.data).first()
                        teste.equipe_id = codigoInput.id
                        db.session.commit()
                        return redirect(url_for('index'))   


                
                # TÁ DANDO ERROOOOOOOOOOOOO
               
                             
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

                # teste do email.
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



@app.route("/apagar/<id>")
@login_required
def apagar(id):
    tartaruga = Tartaruga.query.filter_by(id = id).first()
    db.session.delete(tartaruga)
    db.session.commit()
    return redirect(url_for('historico'))  


@app.route("/teste/<info>")
@app.route("/teste",defaults = {"info":None})
@login_required
def teste(info):
    # print('%02d' % 19)
    
    # i = Tartaruga.query.filter_by(id="1").first()
    # db.session.delete(i)
    db.session.commit()
    return "ok"
