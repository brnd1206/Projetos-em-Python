import mysql.connector

def create_connection():
    conn = mysql.connector.connect(user='root',
                               password='ceub123456',
                               host='127.0.0.1')
    print('Conexão:', conn)
    return conn

def create_database():
   sql_create = '''CREATE DATABASE if not exists db_loja_3'''
   cursor.execute(sql_create)
   sql_use = '''use db_loja_3'''
   cursor.execute(sql_use)

def create_table():
    sql_create = '''CREATE TABLE if not exists tb_produto(
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    nome VARCHAR(50) NOT NULL UNIQUE,
                    preco DECIMAL(9,2) NOT NULL,
                    dt_validade DATE
                    )'''
    cursor.execute(sql_create)

def insert_one():
    var_nome = input("\nInsira o Nome do Produto: ")
    var_preco = input("Insira o Preço do Produto: ")
    var_dt_validade = input("Insira a Data de Validade(aaaa-mm-dd): ")
    sql_insert = f'''INSERT INTO tb_produto
                    (nome, preco, dt_validade)
                    VALUES ('{var_nome}', {var_preco}, '{var_dt_validade}')
                    '''
    cursor.execute(sql_insert)
    con.commit()
    print("\nItem inserido com sucesso!\n")

def select_one():
    pesquisa = input("\nDigite o ID do Produto: ")
    cursor.execute(f'''SELECT *
                    FROM tb_produto
                    WHERE id = {pesquisa}
                    ''')
    registro = cursor.fetchall()
    if not registro:
        print("\nID inválido.\n")
    else:
        for linha in registro:
            print(f"\nID {linha[0]}: {linha[1]}, {linha[2]}, {linha[3]}\n")

def delete_one():
    deletar = input("\nDigite o ID do Produto que deseja excluir: ")
    cursor.execute(f'''DELETE
                    FROM tb_produto
                    WHERE id = {deletar}
                    ''')
    registro = cursor.fetchall()
    if not registro:
        print("\nID inválido.\n")
    else:
        cursor.execute(f'''DELETE FROM tb_produto WHERE id = {deletar}''')
        con.commit()
        print("\nItem deletado com sucesso!\n")

def update_one():
    pesquisa = input("\nDigite o Nome do Produto para atualizar: ")
    novo_preco = input("Digite o novo Preço do Produto: ")
    cursor.execute(f'''UPDATE tb_produto
                    SET preco = {novo_preco}
                    WHERE nome = '{pesquisa}'
                    ''')
    registro = cursor.fetchall()
    if not registro:
        print("\nNome do produto não encontrado.\n")
    else:
        novo_preco = input("Digite o novo Preço do Produto: ")
        cursor.execute(f'''UPDATE tb_produto
                            SET preco = {novo_preco}
                            WHERE nome = '{pesquisa}' ''')
        con.commit()
        print("\nItem atualizado com sucesso!\n")

def close_connection():
    cursor.close()
    con.close()
    print("\nConexão fechada.")

def show_records():
    pesquisa = input("\nDigite o ID do Produto: ")
    cursor.execute(f'''SELECT *
                        FROM tb_produto
                        WHERE id = {pesquisa}
                        ''')
    registro = cursor.fetchall()
    for linha in registro:
        print(f"\n--- ID {linha[0]} ---"
              f"\nNome............: {linha[1]}"
              f"\nPreço...........: RS{linha[2]}"
              f"\nData de Validade: {linha[3]}\n")

if __name__ == '__main__':
    con = create_connection()
    cursor = con.cursor()
    create_database()
    create_table()
    while True:
        crud = input("[i] inserir, [s] selecionar, [d] deletar, [u] atualizar, [e] para sair."
                     "\nSelecione uma das opções: ")
        if crud == 'e':
            close_connection()
            break
        elif crud == 'i':
            insert_one()
        elif crud == 's':
            select_one()
        elif crud == 'd':
            delete_one()
        elif crud == 'u':
            update_one()
        elif crud == 'r':
            show_records()
        else:
            print("Inválido!")