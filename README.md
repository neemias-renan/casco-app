# Casco - Conservação e Proteção de Tartarugas Marinhas

[resumo inicial]

## Como instalar:

Faça um fork do projeto e em seguida clone o repositório forkado por você:

```sh
$ git clone https://github.com/Neemias-Renan/projeto-casco.git
$ cd projeto-casco
```
Use um ambiente virtual para fazer as instalações que serão utilizadas na aplicação:

```sh
$ virtualenv venv
```

Para criar o ambiente virtual com o venv:

```sh
$ python3 -m venv venv
```

Para ativar o ambiente virtual:

```sh
$ source venv/bin/activate       (Linux)
$ source venv\Script\activate    (Windows)
```

E finalmente, instale a lista de pacotes da aplicação:

```sh
$ pip install -r requirements.txt
```
## Configurando o projeto

Atualize o banco de dados:

```sh
$ flask db stamp head
$ flask db migrate -m "atualizando banco de dados"
$ flask db upgrade
```

Para rodar a aplicação utilize o comando:

```sh
$ flask run
```

Acesse no seu navegador o seguinte endereço abaixo:

```sh
http://localhost:5000/
```
