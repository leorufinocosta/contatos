# Funcao para retornar a lista de contatos
def get_contatos(cursor):
    # Executar o SQL
    cursor.execute('SELECT idcontatos, nome, email FROM contatos')

    # Recuperando o retorno do BD
    contatos = cursor.fetchall()

    # Retornar os dados
    return contatos

# Funcao para inserir os dados
def set_contato(cursor, conn, nome, email):
    cursor.execute(f'insert into contatos (nome, email) values("{nome}", "{email}")')
    conn.commit()

# função pra deletar contato
def del_contato(cursor, conn, idcontato):
    cursor.execute(f'delete from conatos where idcontatos = {idcontato}')
    conn.commit()