import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

# ---------- BANCO DE DADOS ----------
def create_connection():
    return mysql.connector.connect(
        user='root',
        password='ceub123456',
        host='127.0.0.1'
    )

def setup_database(cursor):
    cursor.execute("CREATE DATABASE IF NOT EXISTS db_gerenciador")
    cursor.execute("USE db_gerenciador")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tb_usuario (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(50) NOT NULL,
            dt_nasc DATE,
            genero ENUM('M', 'F') NOT NULL
        )""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tb_tarefa (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            status BOOLEAN DEFAULT FALSE
        )""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tb_usuario_tarefa (
            id_usuario INT,
            id_tarefa INT,
            PRIMARY KEY (id_usuario, id_tarefa),
            FOREIGN KEY (id_usuario) REFERENCES tb_usuario(id),
            FOREIGN KEY (id_tarefa) REFERENCES tb_tarefa(id)
        )""")

# ---------- CLASSES ----------
class Usuario:
    def __init__(self, nome, dt_nasc, genero):
        self.nome = nome
        self.dt_nasc = dt_nasc
        self.genero = genero

class Tarefa:
    def __init__(self, nome):
        self.nome = nome

# ---------- FUNÇÕES CRUD ----------
def inserir_usuario(cursor, conn, usuario):
    cursor.execute("""
        INSERT INTO tb_usuario (nome, dt_nasc, genero)
        VALUES (%s, %s, %s)
    """, (usuario.nome, usuario.dt_nasc, usuario.genero))
    conn.commit()

def atualizar_usuario(cursor, conn, id_usuario, nome, dt_nasc, genero):
    cursor.execute("""
        UPDATE tb_usuario
        SET nome = %s, dt_nasc = %s, genero = %s
        WHERE id = %s
    """, (nome, dt_nasc, genero, id_usuario))
    conn.commit()

def deletar_usuario(cursor, conn, id_usuario):
    cursor.execute("DELETE FROM tb_usuario_tarefa WHERE id_usuario = %s", (id_usuario,))
    cursor.execute("DELETE FROM tb_usuario WHERE id = %s", (id_usuario,))
    conn.commit()

def inserir_tarefa(cursor, conn, tarefa):
    cursor.execute("INSERT INTO tb_tarefa (nome) VALUES (%s)", (tarefa.nome,))
    conn.commit()

def atualizar_tarefa(cursor, conn, id_tarefa, novo_nome):
    cursor.execute("UPDATE tb_tarefa SET nome = %s WHERE id = %s", (novo_nome, id_tarefa))
    conn.commit()

def excluir_tarefa(cursor, conn, id_tarefa):
    cursor.execute("DELETE FROM tb_usuario_tarefa WHERE id_tarefa = %s", (id_tarefa,))
    cursor.execute("DELETE FROM tb_tarefa WHERE id = %s", (id_tarefa,))
    conn.commit()

def associar_usuario_tarefa(cursor, conn, id_usuario, id_tarefa):
    cursor.execute("INSERT INTO tb_usuario_tarefa VALUES (%s, %s)", (id_usuario, id_tarefa))
    conn.commit()

def listar_tarefas_por_usuario(cursor):
    cursor.execute("""
        SELECT u.nome, t.id, t.nome, t.status
        FROM tb_usuario u
        JOIN tb_usuario_tarefa ut ON u.id = ut.id_usuario
        JOIN tb_tarefa t ON t.id = ut.id_tarefa
    """)
    return cursor.fetchall()

def listar_tarefas_do_usuario(cursor, id_usuario):
    cursor.execute("""
        SELECT t.id, t.nome, t.status
        FROM tb_tarefa t
        JOIN tb_usuario_tarefa ut ON t.id = ut.id_tarefa
        WHERE ut.id_usuario = %s
    """, (id_usuario,))
    return cursor.fetchall()

def marcar_tarefa_concluida(cursor, conn, id_tarefa):
    cursor.execute("UPDATE tb_tarefa SET status = TRUE WHERE id = %s", (id_tarefa,))
    conn.commit()

def listar_pendentes(cursor):
    cursor.execute("SELECT id, nome FROM tb_tarefa WHERE status = FALSE")
    return cursor.fetchall()

# ---------- INTERFACE TKINTER ----------
class App:
    def __init__(self, master, cursor, conn):
        self.master = master
        self.cursor = cursor
        self.conn = conn
        master.title("Gerenciador de Tarefas")
        master.geometry("600x600")

        self.tabs = ttk.Notebook(master)
        self.tabs.pack(expand=1, fill='both')

        self.tab_usuario()
        self.tab_tarefa()
        self.tab_associar()
        self.tab_listar()
        self.tab_concluir()
        self.tab_pendentes()

    def tab_usuario(self):
        frame = tk.Frame(self.tabs)
        self.tabs.add(frame, text='Gerenciar Usuário')

        tk.Label(frame, text="ID (para atualizar/deletar):").pack()
        self.id_usuario_entry = tk.Entry(frame)
        self.id_usuario_entry.pack()

        tk.Label(frame, text="Nome:").pack()
        self.nome_usuario = tk.Entry(frame)
        self.nome_usuario.pack()

        tk.Label(frame, text="Data de Nasc (YYYY-MM-DD):").pack()
        self.dt_nasc_usuario = tk.Entry(frame)
        self.dt_nasc_usuario.pack()

        tk.Label(frame, text="Gênero (M/F):").pack()
        self.genero_usuario = tk.Entry(frame)
        self.genero_usuario.pack()

        tk.Button(frame, text="Cadastrar", command=self.cadastrar_usuario).pack(pady=5)
        tk.Button(frame, text="Atualizar", command=self.atualizar_usuario).pack(pady=5)
        tk.Button(frame, text="Deletar", command=self.deletar_usuario).pack(pady=5)

    def tab_tarefa(self):
        frame = tk.Frame(self.tabs)
        self.tabs.add(frame, text='Gerenciar Tarefa')

        tk.Label(frame, text="ID da Tarefa (para atualizar/deletar):").pack()
        self.id_tarefa_gerenciar = tk.Entry(frame)
        self.id_tarefa_gerenciar.pack()

        tk.Label(frame, text="Nome da Tarefa:").pack()
        self.nome_tarefa = tk.Entry(frame)
        self.nome_tarefa.pack()

        tk.Button(frame, text="Cadastrar", command=self.cadastrar_tarefa).pack(pady=5)
        tk.Button(frame, text="Atualizar", command=self.atualizar_tarefa).pack(pady=5)
        tk.Button(frame, text="Excluir", command=self.excluir_tarefa).pack(pady=5)

    def tab_associar(self):
        frame = tk.Frame(self.tabs)
        self.tabs.add(frame, text='Associar Tarefa')

        tk.Label(frame, text="ID do Usuário:").pack()
        self.id_usuario = tk.Entry(frame)
        self.id_usuario.pack()

        tk.Label(frame, text="ID da Tarefa:").pack()
        self.id_tarefa = tk.Entry(frame)
        self.id_tarefa.pack()

        tk.Button(frame, text="Associar", command=self.associar).pack(pady=10)

    def tab_listar(self):
        frame = tk.Frame(self.tabs)
        self.tabs.add(frame, text='Listar Tarefas')

        self.lista = tk.Text(frame, height=15)
        self.lista.pack()

        tk.Button(frame, text="Atualizar Lista", command=self.atualizar_lista).pack(pady=10)

    def tab_concluir(self):
        frame = tk.Frame(self.tabs)
        self.tabs.add(frame, text='Marcar Concluída')

        tk.Label(frame, text="ID do Usuário:").pack()
        self.id_usuario_concluir = tk.Entry(frame)
        self.id_usuario_concluir.pack()

        tk.Label(frame, text="ID da Tarefa:").pack()
        self.id_tarefa_concluir = tk.Entry(frame)
        self.id_tarefa_concluir.pack()

        tk.Button(frame, text="Marcar como Concluída", command=self.concluir_tarefa).pack(pady=10)
        tk.Button(frame, text="Listar Tarefas do Usuário", command=self.listar_tarefas_usuario).pack(pady=5)

        self.texto_tarefas_usuario = tk.Text(frame, height=8)
        self.texto_tarefas_usuario.pack()

    def tab_pendentes(self):
        frame = tk.Frame(self.tabs)
        self.tabs.add(frame, text='Tarefas Pendentes')

        self.lista_pendentes = tk.Text(frame, height=15)
        self.lista_pendentes.pack()

        tk.Button(frame, text="Atualizar Pendentes", command=self.atualizar_pendentes).pack(pady=10)

    # ---------- AÇÕES ----------
    def cadastrar_usuario(self):
        try:
            usuario = Usuario(
                self.nome_usuario.get(),
                self.dt_nasc_usuario.get(),
                self.genero_usuario.get().upper()
            )
            inserir_usuario(self.cursor, self.conn, usuario)
            messagebox.showinfo("Sucesso", "Usuário cadastrado!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def atualizar_usuario(self):
        try:
            id_usuario = int(self.id_usuario_entry.get())
            atualizar_usuario(
                self.cursor,
                self.conn,
                id_usuario,
                self.nome_usuario.get(),
                self.dt_nasc_usuario.get(),
                self.genero_usuario.get().upper()
            )
            messagebox.showinfo("Sucesso", "Usuário atualizado!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def deletar_usuario(self):
        try:
            id_usuario = int(self.id_usuario_entry.get())
            deletar_usuario(self.cursor, self.conn, id_usuario)
            messagebox.showinfo("Sucesso", "Usuário deletado!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def cadastrar_tarefa(self):
        try:
            tarefa = Tarefa(self.nome_tarefa.get())
            inserir_tarefa(self.cursor, self.conn, tarefa)
            messagebox.showinfo("Sucesso", "Tarefa cadastrada!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def atualizar_tarefa(self):
        try:
            id_tarefa = int(self.id_tarefa_gerenciar.get())
            novo_nome = self.nome_tarefa.get()
            atualizar_tarefa(self.cursor, self.conn, id_tarefa, novo_nome)
            messagebox.showinfo("Sucesso", "Tarefa atualizada!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def excluir_tarefa(self):
        try:
            id_tarefa = int(self.id_tarefa_gerenciar.get())
            excluir_tarefa(self.cursor, self.conn, id_tarefa)
            messagebox.showinfo("Sucesso", "Tarefa excluída!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def associar(self):
        try:
            id_u = int(self.id_usuario.get())
            id_t = int(self.id_tarefa.get())
            associar_usuario_tarefa(self.cursor, self.conn, id_u, id_t)
            messagebox.showinfo("Sucesso", "Tarefa associada ao usuário!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def atualizar_lista(self):
        self.lista.delete('1.0', tk.END)
        try:
            for u_nome, id_tarefa, t_nome, status in listar_tarefas_por_usuario(self.cursor):
                status_str = "✔" if status else "❌"
                self.lista.insert(tk.END, f"Usuário: {u_nome} | Tarefa: {t_nome} (ID: {id_tarefa}) [{status_str}]\n")
        except Exception as e:
            self.lista.insert(tk.END, "Erro ao carregar tarefas.\n")

    def concluir_tarefa(self):
        try:
            id_usuario = int(self.id_usuario_concluir.get())
            id_tarefa = int(self.id_tarefa_concluir.get())

            self.cursor.execute("""
                SELECT * FROM tb_usuario_tarefa
                WHERE id_usuario = %s AND id_tarefa = %s
            """, (id_usuario, id_tarefa))
            resultado = self.cursor.fetchone()

            if resultado:
                marcar_tarefa_concluida(self.cursor, self.conn, id_tarefa)
                messagebox.showinfo("Sucesso", "Tarefa marcada como concluída.")
            else:
                messagebox.showwarning("Atenção", "Essa tarefa não está associada a esse usuário.")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def listar_tarefas_usuario(self):
        self.texto_tarefas_usuario.delete('1.0', tk.END)
        try:
            id_usuario = int(self.id_usuario_concluir.get())
            tarefas = listar_tarefas_do_usuario(self.cursor, id_usuario)
            for id_t, nome, status in tarefas:
                status_str = "✔" if status else "❌"
                self.texto_tarefas_usuario.insert(tk.END, f"ID: {id_t} | {nome} [{status_str}]\n")
        except Exception as e:
            self.texto_tarefas_usuario.insert(tk.END, "Erro ao listar tarefas.\n")

    def atualizar_pendentes(self):
        self.lista_pendentes.delete('1.0', tk.END)
        try:
            for id_t, nome in listar_pendentes(self.cursor):
                self.lista_pendentes.insert(tk.END, f"ID: {id_t} - {nome}\n")
        except Exception as e:
            self.lista_pendentes.insert(tk.END, "Erro ao listar pendentes.\n")

# ---------- EXECUÇÃO ----------
if __name__ == '__main__':
    conn = create_connection()
    cursor = conn.cursor()
    setup_database(cursor)

    root = tk.Tk()
    app = App(root, cursor, conn)
    root.mainloop()
