import mysql.connector

def create_connection():
    conn = mysql.connector.connect(user='root',
                                   password='ceub123456',
                                   host='127.0.0.1')
    print("Conexão:", conn)
    return conn

def create_database():
    cursor.execute('''CREATE DATABASE if not exists db_garagem''')
    cursor.execute('''USE db_garagem''')

def create_table():
    cursor.execute('''CREATE TABLE if not exists tb_veiculos(
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    placa VARCHAR(10) NOT NULL UNIQUE,
                    modelo VARCHAR(100) NOT NULL,
                    dt_aquisicao DATE,
                    valor DECIMAL(10,2)
                    )''')

def insert_one():
    placa = input("\nInsira a Placa: ")
    modelo = input("Insira o Modelo: ")
    dt = input("Insira a Data de Aquisição(aaaa-mm-dd): ")
    valor = input("Insira o Valor(R$): ")
    cursor.execute(f'''INSERT INTO tb_veiculos
                    (placa, modelo, dt_aquisicao, valor)
                    VALUES ('{placa}', '{modelo}', '{dt}', {valor})
                    ''')
    con.commit()

def select_all():
    cursor.execute('''SELECT * FROM tb_veiculos
                    ''')
    registros = cursor.fetchall()
    for linha in registros:
        print(f"\n-- ID {linha[0]} --"
              f"\nPlaca............: {linha[1]}"
              f"\nModelo...........: {linha[2]}"
              f"\nData de Aquisição: {linha[3]}"
              f"\nPreço............: R${linha[4]}")

def select_one():
    pesquisa = input("\nDigite o ID do Veículo: ")
    cursor.execute(f'''SELECT * FROM tb_veiculos
                        WHERE id = {pesquisa}
                        ''')
    registros = cursor.fetchall()
    for linha in registros:
        print(f"\n-- ID {linha[0]} --"
              f"\nPlaca............: {linha[1]}"
              f"\nModelo...........: {linha[2]}"
              f"\nData de Aquisição: {linha[3]}"
              f"\nPreço............: R${linha[4]}")

def crud():
    while True:
        crud = input("\n[i] inserir, [s] selecionar, [e] para sair."
                     "\nSelecione uma das opções: ")
        if crud == 'e':
            cursor.close()
            con.close()
            break
        elif crud == 'i':
            insert_one()
        elif crud == 's':
            escolha = input("Deseja ver todos? [s]/[n]\n")
            if escolha == 's':
                select_all()
            elif escolha == 'n':
                select_one()
            else:
                print("Inválido!")
        else:
            print("Inválido!")

if __name__ == '__main__':
    con = create_connection()
    cursor = con.cursor()
    create_database()
    create_table()
    crud()