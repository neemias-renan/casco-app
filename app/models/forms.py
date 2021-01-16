from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField,BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField("email", validators = [DataRequired()])
    senha = PasswordField("senha", validators = [DataRequired()])

class CadastroLiderForm(FlaskForm):
    nome = StringField("nome", validators = [DataRequired()])
    email = StringField("email", validators = [DataRequired()])
    senha = PasswordField("senha", validators = [DataRequired()])
    confirmarSenha = PasswordField("confirmarSenha", validators = [DataRequired()])

class CadastroPesquisadorForm(FlaskForm):
    nome = StringField("nome", validators = [DataRequired()])
    email = StringField("email", validators = [DataRequired()])
    senha = PasswordField("senha", validators = [DataRequired()])
    confirmarSenha = PasswordField("confirmarSenha", validators = [DataRequired()])

class CadastroEquipeForm(FlaskForm):
    nomedaEquipe = StringField("nomedaEquipe", validators = [DataRequired()])
    

