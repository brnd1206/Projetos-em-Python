# Gerenciador de Tarefas com Tkinter e MySQL

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg) ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Um projeto simples de um sistema de gerenciamento de tarefas desenvolvido em Python, utilizando a biblioteca `Tkinter` para a interface gráfica e `MySQL` como banco de dados. A aplicação permite o cadastro de usuários, criação de tarefas, associação de tarefas a usuários e o acompanhamento do status de cada tarefa (pendente ou concluída).

## Screenshot

É altamente recomendável adicionar um screenshot da aplicação para que os visitantes possam ver como ela é.

![Screenshot da Aplicação](https://i.imgur.com/your-image-url.png)
*(Substitua o link acima por um screenshot real da sua aplicação)*

## Funcionalidades

O sistema é organizado em abas para facilitar a navegação e o uso:

* **👤 Gerenciar Usuário:**
    * Cadastrar novos usuários (Nome, Data de Nascimento, Gênero).
    * Atualizar informações de um usuário existente pelo seu ID.
    * Deletar um usuário e todas as suas associações de tarefas.

* **📝 Gerenciar Tarefa:**
    * Cadastrar novas tarefas.
    * Atualizar o nome de uma tarefa existente pelo seu ID.
    * Excluir uma tarefa do sistema.

* **🔗 Associar Tarefa:**
    * Vincular uma tarefa existente a um usuário específico usando seus respectivos IDs.

* **📋 Listar Tarefas:**
    * Exibir uma lista completa de todas as tarefas associadas a todos os usuários, indicando o status (✔ para concluída, ❌ para pendente).

* **✅ Marcar Concluída:**
    * Listar todas as tarefas de um usuário específico.
    * Marcar uma tarefa como concluída.

* **⏳ Tarefas Pendentes:**
    * Exibir uma lista de todas as tarefas no sistema que ainda não foram concluídas.

## Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Interface Gráfica:** Tkinter (biblioteca padrão do Python)
* **Banco de Dados:** MySQL
* **Conector:** `mysql-connector-python`

## Pré-requisitos

Antes de rodar o projeto, você precisa ter instalado:

1.  **Python 3.8 ou superior.**
2.  **Um servidor MySQL** (local ou remoto) em execução. Você pode usar XAMPP, WAMP, Docker ou uma instalação nativa do MySQL.
3.  **A biblioteca `mysql-connector-python`**. Para instalar, use o pip:
    ```bash
    pip install mysql-connector-python
    ```

## Como Instalar e Executar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    cd seu-repositorio
    ```

2.  **Configure a Conexão com o Banco de Dados:**
    Abra o arquivo de código e localize a função `create_connection()`. Altere os parâmetros `user`, `password` e `host` para corresponder às suas credenciais do MySQL.

    ```python
    def create_connection():
        return mysql.connector.connect(
            user='seu_usuario_mysql',      # <- ALTERE AQUI
            password='sua_senha_mysql',  # <- ALTERE AQUI
            host='127.0.0.1'             # <- Altere se seu BD não for local
        )
    ```

3.  **Execute o script:**
    O script criará automaticamente o banco de dados `db_gerenciador` e as tabelas necessárias na primeira execução.

    ```bash
    python nome_do_seu_arquivo.py
    ```

## Estrutura do Banco de Dados

O sistema utiliza três tabelas para organizar os dados:

* `tb_usuario`: Armazena as informações dos usuários.
    * `id` (PK, INT, AUTO_INCREMENT)
    * `nome` (VARCHAR)
    * `dt_nasc` (DATE)
    * `genero` (ENUM 'M', 'F')

* `tb_tarefa`: Armazena as tarefas.
    * `id` (PK, INT, AUTO_INCREMENT)
    * `nome` (VARCHAR)
    * `status` (BOOLEAN)

* `tb_usuario_tarefa`: Tabela de associação (relação N:N) que conecta usuários a tarefas.
    * `id_usuario` (FK para `tb_usuario.id`)
    * `id_tarefa` (FK para `tb_tarefa.id`)

## Contribuição

Contribuições são bem-vindas! Se você tiver alguma ideia para melhorar o projeto, sinta-se à vontade para criar um *fork* do repositório e enviar um *Pull Request*.
