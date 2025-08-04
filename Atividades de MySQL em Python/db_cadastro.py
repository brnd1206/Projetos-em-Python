import mysql.connector

def create_connection():
    conexao = mysql.connector.connect(user='root',
                                      password ='ceub123456',
                                      host='127.0.0.1')
    print("Conexão:", conexao)
    return conexao

def create_database():
    cursor.execute('''CREATE DATABASE if not exists db_cadastro''')
    cursor.execute('''USE db_cadastro''')

def create_table():
    cursor.execute('''CREATE TABLE if not exists tb_cargo(
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    nome VARCHAR(50) NOT NULL UNIQUE
                    )''')

    cursor.execute('''CREATE TABLE if not exists tb_empregado(
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    nome VARCHAR(50) NOT NULL,
                    dt_nasc DATE,
                    genero ENUM('M', 'F') NOT NULL,
                    cod_cargo INT,
                    FOREIGN KEY (cod_cargo) REFERENCES tb_cargo(id)
                    )''')

def insert_one():
    insert = input("\nDeseja inserir no cargo[c] ou empregado[e]: ")
    if insert == 'c':
        v_nome = input("\nInsira o Nome do Cargo: ")
        cursor.execute(f'''INSERT INTO tb_cargo
                        (nome)
                        VALUES ('{v_nome}')
                        ''')
        conn.commit()
    elif insert == 'e':
        v_nome = input("\nInsira o Nome: ")
        v_dt_nasc = input("Insira a Data de Nascimento(aaaa-mm-dd): ")
        v_genero = input("Insira o Gênero: ").upper()
        v_cod = input("Insira o Código do Cargo: ")
        cursor.execute(f'''INSERT INTO tb_empregado
                            (nome, dt_nasc, genero, cod_cargo)
                            VALUES ('{v_nome}', '{v_dt_nasc}', '{v_genero}', {v_cod})
                            ''')
        conn.commit()
    else:
        print("\nInválido!")

def select_all():
    select = input("\nDeseja ver a tabela cargo[c] ou empregado[e]: ")
    if select == 'c':
        cursor.execute('''SELECT * FROM tb_cargo''')
        for linha in cursor.fetchall():
            print(f"\n-- ID {linha[0]} --"
                  f"\nNome do Cargo: {linha[1]}")
    elif select == 'e':
        cursor.execute('''SELECT tb_empregado.id, tb_empregado.nome, tb_empregado.dt_nasc,
                            tb_empregado.genero, tb_cargo.nome
                        FROM tb_empregado
                        JOIN tb_cargo ON tb_empregado.cod_cargo = tb_cargo.id
                        ''')
        for linha in cursor.fetchall():
            print(f"\n-- ID {linha[0]} --"
                  f"\nNome..............: {linha[1]}"
                  f"\nData de Nascimento: {linha[2]}"
                  f"\nGênero............: {linha[3]}"
                  f"\nCargo.............: {linha[4]}")
    else:
        print("\nInválido!")

def select_one():
    select = input("\nDeseja ver a tabela cargo[c] ou empregado[e]: ")
    if select == 'c':
        pesquisa = input("\nDigite o ID que deseja pesquisar: ")
        cursor.execute(f'''SELECT * FROM tb_cargo
                        WHERE id = {pesquisa}
                        ''')
        for linha in cursor.fetchall():
            print(f"\n-- ID {linha[0]} --"
                  f"\nNome..............: {linha[1]}"
                  f"\nData de Nascimento: {linha[2]}"
                  f"\nGênero............: {linha[3]}"
                  f"\nCódigo do Cargo...: {linha[4]}")
    elif select == 'e':
        pesquisa = input("\nDigite o ID que deseja pesquisar: ")
        cursor.execute(f'''SELECT tb_empregado.id, tb_empregado.nome, tb_empregado.dt_nasc,
                                tb_empregado.genero, tb_cargo.nome
                            FROM tb_empregado
                            JOIN tb_cargo ON tb_empregado.cod_cargo = tb_cargo.id
                            WHERE tb_empregado.id = {pesquisa}        
                        ''')
        for linha in cursor.fetchall():
            print(f"\n-- ID {linha[0]} --"
                  f"\nNome..............: {linha[1]}"
                  f"\nData de Nascimento: {linha[2]}"
                  f"\nGênero............: {linha[3]}"
                  f"\nCódigo do Cargo...: {linha[4]}")
    else:
        print("\nInválido!")

def delete_one():
    insert = input("\nDeseja deletar no cargo[c] ou empregado[e]: ")
    if insert == 'c':
        deletar = input("Insira o Nome que deseja exluir: ")
        cursor.execute(f'''DELETE FROM tb_cargo
                        WHERE nome = '{deletar}'
                        ''')
        conn.commit()
    elif insert == 'e':
        deletar = input("Insira o Nome que deseja exluir: ")
        cursor.execute(f'''DELETE FROM tb_empregado
                        WHERE nome = '{deletar}'
                        ''')
        conn.commit()
    else:
        print("\nInválido!")

if __name__ == '__main__':
    conn = create_connection()
    cursor = conn.cursor()
    create_database()
    create_table()

    while True:
        crud = int(input("\n[1] Inserir"
                     "\n[2] Selecionar"
                     "\n[3] Deletar"
                     "\n[4] Atualizar"
                     "\n[5] Sair"
                     "\nSelecione uma das opções: "))
        if crud == 5:
            cursor.close()
            conn.close()
            break
        elif crud == 1:
            insert_one()
        elif crud == 2:
            selecionar = input("\nDeseja ver todos? [s/n]"
                               "\nInsira: ")
            if selecionar == 's':
                select_all()
            elif selecionar == 'n':
                select_one()
            else:
                print("\nInválido!")
        elif crud == 3:
            delete_one()
        else:
            print("\nInválido!")