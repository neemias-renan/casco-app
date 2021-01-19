# Casco - Conservação e Proteção de Tartarugas Marinhas

A plataforma (Casco) surgiu em 2020 com o objetivo de auxiliar biólogos ao monitoramento de tartarugas marinhas e disponibilizar os dados coletados para futuras pesquisas científicas. O projeto é mantido pelos estudantes Neemias Renan e Hortência Arliane, orientado pelo Prof. Me. Pedro Baesse e originalmente desenvolvido no IFRN.

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
No Linux:

$ source venv/bin/activate      

No Windows:

$ cd venv\Script\  
  em seguida digite: 
$ activate
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
