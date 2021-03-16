# Casco - Conservação e Proteção de Tartarugas Marinhas

A plataforma (Casco) surgiu em 2020 com o objetivo de auxiliar biólogos ao monitoramento de tartarugas marinhas e disponibilizar os dados coletados para futuras pesquisas científicas. O projeto é mantido pelo estudante Neemias Renan, orientado pelo Prof. Me. Pedro Baesse e originalmente desenvolvido no IFRN.

## Como instalar:

Use um ambiente virtual para fazer as instalações que serão utilizadas na aplicação:

Na pasta do projeto instale o ambiente virtual:

```sh
$ pip install virtualenv
```
em seguida inicialize o ambiente virtual digite:
```sh
$ virtualenv -p python3 venv
```

Para ativar o ambiente virtual:

No Windows:
```
$ cd venv\Scripts\  
```
  em seguida digite: 
```
$ activate
```

Volte para a pasta inicial do projeto, e finalmente, instale a lista de pacotes da aplicação:

```sh
$ pip3 install -r requirements.txt
```
## Configurando o projeto
Se na pasta principal do projeto existir a pasta migrate e o banco 'storage.db', pule a seguinte etapa:

Crie o banco de dados:

```sh
$ py run.py db init
$ py run.py db migrate
```
Apenas se já existir a pasta migrate execute o seguinte código:
```
$ py run.py db upgrade
```

Para rodar a aplicação utilize o comando:

```sh
$ py run.py runserver
```

Acesse no seu navegador o seguinte endereço abaixo:

```sh
http://localhost:5000/
```
