from app import db
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class User(db.Model):
    __tablename__ = "users"


    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String)
    email = db.Column(db.String, unique = True)
    senha = db.Column(db.String)
    tipo = db.Column(db.String(11))
    equipe_id = db.Column(db.Integer, db.ForeignKey('equipes.id'))
    equipes = db.relationship("Equipe",backref=db.backref("users",lazy=True))

    
    # lider / pesquisador

    @property
    def is_authenticated(self):
        return True
    @property
    def is_active(self):
        return True
    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, nome, email, senha,tipo,equipes):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo = tipo
       
        if tipo == "pesquisador":
            self.equipes = None
        else:
            self.equipes = equipes
        

    
    def __repr__(self):
        return "%r,%r" % (self.nome, self.email)

class Equipe(db.Model):
    __tablename__ = "equipes"
    id = db.Column(db.Integer, primary_key = True)
    nomedaequipe = db.Column(db.String, unique = True)
    codigodaequipe = db.Column(db.String, unique = True)
    # users = db.relationship("User",backref=db.backref("equipe",lazy=True))
    

    def __init__(self, nomedaequipe,codigodaequipe):
        self.nomedaequipe = nomedaequipe
        self.codigodaequipe = codigodaequipe
        

     
    def __repr__(self):
        return "%r" % (self.nomedaequipe)

class Tartaruga(db.Model):
    __tablename__ = "tartarugas"

    id = db.Column(db.Integer, primary_key = True)
    anilha = db.Column(db.String)
    informacoes = db.Column(db.Text)
    especie = db.Column(db.String)
    tipo_de_registro = db.Column(db.String)
    monitoramento = db.Column(db.String(3))
    sexo = db.Column(db.String(2))
    ccc = db.Column(db.String(5))
    lcc = db.Column(db.String(5))
    municipio = db.Column(db.String)
    praia = db.Column(db.String)
    latitude = db.Column(db.String)
    longitude = db.Column(db.String)
    data = db.Column(db.String)
    hora = db.Column(db.String)

    datadoalerta = db.Column(db.String)
    
    # equipe_id = db.Column(db.Integer, db.ForeignKey('equipes.id'),unique = True)

    # equipe = db.relationship('Equipe',foreign_keys = equipe_id)

    def __init__(self, anilha,informacoes,especie,tipo_de_registro, sexo,ccc,lcc,municipio,praia,latitude,longitude,data,hora,datadoalerta):
        self.anilha = anilha
        self.informacoes = informacoes
        self.especie = especie
        self.tipo_de_registro = tipo_de_registro
        self.sexo = sexo
        self.ccc = ccc
        self.lcc = lcc
        self.municipio = municipio
        self.praia = praia
        self.latitude = latitude
        self.longitude = longitude
        self.data = data
        self.hora = hora
        self.datadoalerta = datadoalerta
        # self.equipe_id = equipe_id
    
    def __repr__(self):
        return "Anilha = '%s', Informações de Registro = '%s', Espécie = '%s', Tipo de Registro = '%s', Sexo = '%s', CCC = '%s', LCC = '%s', Município = '%s', Praia = '%s', Latitude = '%s', Longitude = '%s', Data do registro = '%s', Hora do registro = '%s'" % (self.anilha, self.informacoes, self.especie, self.tipo_de_registro, self.sexo, self.ccc, self.lcc, self.municipio, self.praia, self.latitude, self.longitude, self.data, self.hora)

class Nova_Desova(db.Model):
    __tablename__ = "novas_desovas"

    id = db.Column(db.Integer, primary_key = True)
    municipio = db.Column(db.String)
    praia = db.Column(db.String)
    latitude = db.Column(db.String)
    longitude = db.Column(db.String)
    data = db.Column(db.String)
    hora = db.Column(db.String)
    datadoalerta = db.Column(db.String)

    def __init__(self,municipio,praia,latitude,longitude,data,hora,datadoalerta):
        self.municipio = municipio
        self.praia = praia
        self.latitude = latitude
        self.longitude = longitude
        self.data = data
        self.hora = hora
        self.datadoalerta = datadoalerta
    
    def __repr__(self):
        return "Nova desova %r" % self.id 