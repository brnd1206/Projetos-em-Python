import mysql.connector

def create_connection():
    conn = mysql.connector.connect(user='root',
                                   password='ceub123456',
                                   host='127.0.0.1')
    print('Conexão:', conn)
    return conn

def create_database():
    cursor.execute('CREATE DATABASE if not exists db_clinica')
    cursor.execute('USE db_clinica')

def create_table():
    cursor.execute('''CREATE TABLE if not exists tb_pacientes(
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    cpf CHAR(14) NOT NULL UNIQUE,
                    nome VARCHAR(50) NOT NULL,
                    peso DECIMAL(5,2),
                    altura DECIMAL(4,2),
                    data_nascimento DATE)
                    ''')

def insert_one():
    v_cpf = input("\nInsira o CPF: ")
    v_nome = input("Insira o Nome: ")
    v_peso = input("Insira o Peso(kg): ")
    v_altura = input("Insira a Altura(m): ")
    v_nasc = input("Insira a Data de Nascimento: ")

    cursor.execute(f'''INSERT INTO tb_pacientes
                    (cpf, nome, peso, altura, data_nascimento)
                    VALUES ('{v_cpf}', '{v_nome}', {v_peso}, {v_altura}, '{v_nasc}')''')
    con.commit()


def select_all():
    cursor.execute(f'''SELECT * FROM tb_pacientes''')
    registros = cursor.fetchall()
    for i, linha in enumerate(registros, 1):
        print(f"\n-- Paciente {i} --")
        print(f"CPF.......: {linha[1]}")
        print(f"Nome......: {linha[2]}")
        print(f"Peso......: {linha[3]}kg")
        print(f"Altura....: {linha[4]}m")
        print(f"Nascimento: {linha[5]}")

def select_one():
    pesquisa = input("\nDigite o CPF: ")
    cursor.execute(f'''SELECT * FROM tb_pacientes
                    WHERE cpf = '{pesquisa}'
                    ''')
    registros = cursor.fetchall()
    for i, linha in enumerate(registros, 1):
        print(f"\n-- Paciente {i} --")
        print(f"CPF.......: {linha[1]}")
        print(f"Nome......: {linha[2]}")
        print(f"Peso......: {linha[3]}kg")
        print(f"Altura....: {linha[4]}m")
        print(f"Nascimento: {linha[5]}")

def delete_one():
    deletar = input("\nInsira o CPF que deseja excluir: ")
    cursor.execute(f'''DELETE FROM tb_pacientes
                    WHERE cpf = '{deletar}'
                    ''')
    con.commit()

def crud():
    while True:
        crud = input("\n[i] inserir, [s] selecionar, [d] deletar, [e] para sair."
                     "\nSelecione uma das opções: ")
        if crud == 'e':
            cursor.close()
            con.close()
            break
        elif crud == 'i':
            insert_one()
        elif crud == 's':
            escolha = input("\nDeseja ver todos? [s]/[n]"
                            "\nInsira: ")
            if escolha == 's':
                select_all()
            elif escolha == 'n':
                select_one()
            else:
                print("Inválido!")
        elif crud == 'd':
            delete_one()
        else:
            print("Inválido!")

if __name__ == '__main__':
    con = create_connection()
    cursor = con.cursor()
    create_database()
    create_table()
    crud()
