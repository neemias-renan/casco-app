
from app.models.tables import Equipe, User, Tartaruga,Nova_Desova
from datetime import date,timedelta

def exibirNomedoUsuario(nomedousuario):
    nomeCompleto = nomedousuario
    nomeCompleto_Split = nomeCompleto.split(" ")
    primeiro_Nome = nomeCompleto_Split[0]
    return primeiro_Nome

def exibirNomedaEquipe(iddaEquipe):
    id_equipe = iddaEquipe
    nomedaEquipe = Equipe.query.filter_by(id = id_equipe).first()
    return nomedaEquipe

def exibirMembrosdaEquipe(iddaEquipe):
    id_equipe = iddaEquipe
    membrosdaEquipe = User.query.filter_by(equipe_id = iddaEquipe).all() 
    return membrosdaEquipe

def exibirNomedoLiderdaEquipe(iddaEquipe):
    lider = User.query.filter_by(equipe_id = iddaEquipe).first()
    nomedoLider = lider.nome
    return nomedoLider

def exibirDatadeHoje():
    datadeHoje = str(date.today())
    # Formato {Ano-Mês-Dia}
    arraydaDatadeHoje = datadeHoje.split("-")
    # Reposicionamento da data
    dia = int(arraydaDatadeHoje[2])
    mes = int(arraydaDatadeHoje[1])
    ano = int(arraydaDatadeHoje[0])
    # Formato {Dia-Mês-Ano}
    
    datadeHojeReformulada = str("%r/%r/%r" %('%02d' % dia,'%02d' % mes, ano))
    eliminarAspas = "'"
    
    for i in range(0,len(eliminarAspas)):
        datadeHojeReformulada = datadeHojeReformulada.replace(datadeHojeReformulada[i],"")

    return datadeHojeReformulada

def realizarCorrecaodeDataOriginal(data):
    arraydaDataOriginal = data.split("-")
    # Formato {Ano-Mês-Dia}

    ano = int(arraydaDataOriginal[0])
    mes = int(arraydaDataOriginal[1])
    dia = int(arraydaDataOriginal[2])

    dataOriginalReformulada = str("%s/%s/%s" %('%02d' % dia,'%02d' % mes,'%02d' % ano))
    # Formato {Dia-Mês-Ano}

    return dataOriginalReformulada

def realizarCorrecaodeDatadeFuturoAlerta(data):
    arraydaDataOriginal = data.split("-")
    # Formato {Ano-Mês-Dia}
    anoOriginal = int(arraydaDataOriginal[0])
    mesOriginal = int(arraydaDataOriginal[1])
    diaOriginal = int(arraydaDataOriginal[2])
    
    datadoFuturoAlerta = str(date(anoOriginal,mesOriginal,diaOriginal) + timedelta(days = 2))

    # ******************************LEMBRAR DE TROCAR PARA 45 DIAS*****
    arraydaDatadoFuturoAlerta = datadoFuturoAlerta.split("-")

    ano = int(arraydaDatadoFuturoAlerta[0])
    mes = int(arraydaDatadoFuturoAlerta[1])
    dia = int(arraydaDatadoFuturoAlerta[2])

    datadoFuturoAlertaReformulada = str("%s/%s/%s"%('%02d' %dia,'%02d' %mes,'%02d' %ano))

    return datadoFuturoAlertaReformulada