# Importando bibliotecas
from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
from bd import *

# Instanciando a app Flask
app = Flask(__name__)
# Instanciar o objeto MySQL
mysql = MySQL()
# Ligar o MYSQL ao Flask
mysql.init_app(app)

# Configurando o acesso ao MySQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'contatos'

# Rota para /
@app.route('/')
def principal():
    return render_template('index.html')

# Rota para /listar
@app.route('/listar')
def listar():
    # Obtendo o cursor para acessar o BD
    conn = mysql.connect()
    cursor = conn.cursor()

    contatos = get_contatos(cursor)

    # Fechar o cursor
    cursor.close()
    # Fechar a conexao
    conn.close()

    return render_template('listar.html', contatos=contatos)

# rota para o formulário de inserção
@app.route('/form_inserir')
def form_inserir():
    return render_template('form_inserir.html')

# rota para inserir os dados
@app.route('/inserir', methods=['post'])
def inserir():
    if request.method == 'POST':
        # recuperar os parametros
        nome = request.form.get('nome')
        email = request.form.get('email')

        # Obtendo o cursor para acessar o BD
        conn = mysql.connect()
        cursor = conn.cursor()

        # inserindo o contato
        set_contato(cursor, conn, nome, email)

        # Fechar o cursor
        cursor.close()
        # Fechar a conexao
        conn.close()

        # retornando a lista de contatos
        return redirect(url_for('listar'))

    else:
        form_inserir()

@app.route('/deletar/<idcontato>')
def deletar(idcontato):
    conn = mysql.connect()
    cursor = conn.cursor()

    del_contato(cursor, conn, idcontato)

    cursor.close()
    conn.close()
    return render_template('listar.html', delete=del_contato)

# Rodando a app
if __name__ == '__main__':
    app.run(debug=True)