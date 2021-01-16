from app import db

class Lider(db.Model):
    __tablename__ = "lideres"

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String)
    email = db.Column(db.String, unique = True)
    senha = db.Column(db.String)
    lider = db.relationship('Equipe', backref ="lideres", lazy = "dynamic")

    # @property
    # def is_authenticated(self):
    #     return True
    # @property
    # def is_active(self):
    #     return True
    # @property
    # def is_anonymous(self):
    #     return False

    # def get_id(self):
    #     return str(self.id)

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
    
    def __repr__(self):
        return "<Lider %r>" % self.nome

class Pesquisador(db.Model):
    __tablename__ = "pesquisadores"

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String)
    email = db.Column(db.String, unique = True)
    senha = db.Column(db.String)
      
    pesquisador = db.relationship('Equipe',backref ="pesquisadores", lazy = "dynamic")

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
    
    def __repr__(self):
        return "<Pesquisador %r>" % self.nome

class Equipe(db.Model):
    __tablename__ = "equipes"

    id = db.Column(db.Integer, primary_key = True)
    nomedaequipe = db.Column(db.String, unique = True)
    lider_id = db.Column(db.Integer, db.ForeignKey('lideres.id'),unique = True)
    pesquisador_id = db.Column(db.Integer, db.ForeignKey('pesquisadores.id'),unique = True)

  

    def __init__(self, nomedaEquipe, lider_id, pesquisador_id):
        self.nomedaEquipe = nomedaEquipe
        self.lider_id = lider_id
        self.pesquisador_id = pesquisador_id 

     
    def __repr__(self):
        return "<Equipe %r>" % self.nomedaEquipe

class Tartaruga(db.Model):
    __tablename__ = "tartarugas"

    id = db.Column(db.Integer, primary_key = True)
    anilha = db.Column(db.String, unique = True)
    especie = db.Column(db.String)
    tipo_de_registro = db.Column(db.String)
    sexo = db.Column(db.String(2))
    ccc = db.Column(db.String(5))
    lcc = db.Column(db.String(5))
    informacoes = db.Column(db.Text)
    municipio = db.Column(db.String)
    praia = db.Column(db.String)
    latitude = db.Column(db.String)
    longitude = db.Column(db.String)
    data = db.Column(db.String)
    hora = db.Column(db.String)
    monitoramento = db.Column(db.String(3))
    equipe_id = db.Column(db.Integer, db.ForeignKey('equipes.id'),unique = True)

    equipe = db.relationship('Equipe',foreign_keys = equipe_id)

    def __init__(self, anilha,especie,tipo_de_registro,sexo,ccc,lcc,informacoes,municipio,praia,latitude,longitude,data,hora, monitoramento, equipe_id):
        self.anilha = anilha
        self.especie = especie
        self.tipo_de_registro = tipo_de_registro
        self.sexo = sexo
        self.ccc = ccc
        self.lcc = lcc
        self.informacoes = informacoes
        self.municipio = municipio
        self.praia = praia
        self.latitude = latitude
        self.longitude = longitude
        self.data = data
        self.hora = hora
        self.monitoramento = monitoramento
        self.equipe_id = equipe_id
    
    def __repr__(self):
        return "<Tartaruga %r>" % self.anilha


class Nova_Desova(db.Model):
    __tablename__ = "novas_desovas"

    id = db.Column(db.Integer, primary_key = True)
    municipio = db.Column(db.String)
    praia = db.Column(db.String)
    latitude = db.Column(db.String)
    longitude = db.Column(db.String)
    data = db.Column(db.String)
    hora = db.Column(db.String)
    monitoramento = db.Column(db.String(3))
    equipe_id = db.Column(db.Integer, db.ForeignKey('equipes.id'),unique = True)

    equipe = db.relationship('Equipe',foreign_keys = equipe_id)

    def __init__(self,municipio,praia,latitude,longitude,data,hora, monitoramento, equipe_id):
        self.municipio = municipio
        self.praia = praia
        self.latitude = latitude
        self.longitude = longitude
        self.data = data
        self.hora = hora
        self.monitoramento = monitoramento
        self.equipe_id = equipe_id
    
    def __repr__(self):
        return "<Nova desova %r>" % self.id 