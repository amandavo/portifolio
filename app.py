from flask import Flask, render_template, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

#Conexão com o Banco de Dados
app.config['MYSQL_HOST'] = 'localhost' # = 127.0.0.1
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'portifolio'

mysql = MySQL(app)


@app.route("/")
@app.route("/index")
def home():
    return render_template("home.html")



@app.route("/contato", methods=['GET', 'POST'])
def contato():
    if request.method == "POST":
        nome = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        txtdesc = request.form['txtdesc']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO CONTATO (nome, email, assunto, txtdesc) VALUES (%s, %s, %s, %s)", (nome, email, assunto, txtdesc) )

        mysql.connection.commit()
        cur.close()

        return "Cadastro feito com Sucesso!"
    return render_template("contato.html")


@app.route("/dados")
def dados():
    cur = mysql.connection.cursor()

    contato = cur.execute("select * from contato")

    if contato > 0:
        contatoDetails = cur.fetchall()

        return render_template("tabela.html", contatoDetails=contatoDetails)
