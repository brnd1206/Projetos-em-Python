from datetime import datetime  # Importa o módulo datetime para trabalhar com datas

# Definindo a classe Endereco para representar um endereço
class Endereco:
    # Inicializa a instância com cidade e estado (estado tem valor padrão 'DF')
    def __init__(self, cidade, estado='DF'):
        self.cidade = cidade  # Atribui o valor de cidade
        self.estado = estado  # Atribui o valor de estado (valor padrão 'DF')

    # Método para obter a cidade
    def get_cidade(self):
        return self.cidade

    # Método para definir uma nova cidade
    def set_cidade(self, nova_cidade):
        self.cidade = nova_cidade

    # Método para obter o estado
    def get_estado(self):
        return self.estado

    # Método para definir um novo estado
    def set_estado(self, novo_estado):
        self.estado = novo_estado

    # Representação em string do objeto Endereco
    def __str__(self):
        return f"{self.cidade} - {self.estado}"  # Retorna o endereço no formato "cidade - estado"

# Definindo a classe Cliente para representar um cliente
class Cliente:
    # Inicializa a instância com nome, ano de nascimento e uma lista de endereços vazia
    def __init__(self, nome, ano_nascimento):
        self.nome = nome  # Atribui o nome do cliente
        self.ano_nascimento = ano_nascimento  # Atribui o ano de nascimento
        self.enderecos = []  # Lista que armazenará os endereços do cliente

    # Método para obter o nome do cliente
    def get_nome(self):
        return self.nome

    # Método para definir um novo nome para o cliente
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    # Método para obter o ano de nascimento do cliente
    def get_ano_nascimento(self):
        return self.ano_nascimento

    # Método para definir um novo ano de nascimento
    def set_ano_nascimento(self, novo_ano_nascimento):
        self.ano_nascimento = novo_ano_nascimento

    # Método para calcular a idade do cliente com base no ano atual
    def calcula_idade(self):
        return datetime.now().year - self.ano_nascimento  # Subtrai o ano de nascimento do ano atual

    # Método para inserir um novo endereço na lista de endereços do cliente
    def insere_endereco(self, cidade, estado='DF'):
        endereco = Endereco(cidade, estado)  # Cria um novo objeto Endereco
        self.enderecos.append(endereco)  # Adiciona o endereço à lista de endereços

    # Método para remover um endereço da lista de endereços do cliente
    def remove_endereco(self, cidade, estado='DF'):
        endereco = Endereco(cidade, estado)  # Cria um novo objeto Endereco
        self.enderecos.remove(endereco)  # Remove o endereço da lista de endereços

    # Método para mostrar todos os endereços cadastrados para o cliente
    def mostra_enderecos(self):
        print(f"Endereço(s) de {self.nome}:")
        for endereco in self.enderecos:
            print(endereco)  # Exibe cada endereço na lista de endereços

    # Método para inserir um endereço já existente (objeto Endereco)
    def insere_endereco2(self, endereco):
        self.enderecos.append(endereco)  # Adiciona o endereço à lista de endereços

    # Método para remover um endereço já existente (objeto Endereco)
    def remove_endereco2(self, endereco):
        self.enderecos.remove(endereco)  # Remove o endereço da lista de endereços

    # Método para mostrar os endereços de maneira diferente, usando formatação
    def mostra_enderecos2(self):
        for endereco in self.enderecos:
            print(f"{endereco}")  # Exibe cada endereço de forma formatada

    # Representação em string do objeto Cliente
    def __str__(self):
        idade = self.calcula_idade()  # Calcula a idade do cliente
        result = (f"Cliente: {self.nome}\n"
                  f"Idade: {idade} anos\n")  # Formata o nome e a idade do cliente
        if self.enderecos:
            result += f"Endereço(s) de {self.nome}:\n"
            for endereco in self.enderecos:
                result += f"• {endereco}\n"  # Adiciona os endereços à string result
        else:
            result += "Nenhum endereço cadastrado."  # Caso não haja endereços, exibe uma mensagem
        return result  # Retorna a string formatada

# Bloco principal para testar as classes
if __name__ == '__main__':
    cliente1 = Cliente("João", 1990)  # Cria um novo cliente com nome "João" e ano de nascimento 1990
    cliente1.insere_endereco("Brasília")  # Adiciona um endereço para o cliente com a cidade "Brasília"
    endereco1 = Endereco("São Paulo", "SP")  # Cria um novo endereço para "São Paulo" com estado "SP"
    cliente1.insere_endereco2(endereco1)  # Adiciona o endereço criado anteriormente
    cliente1.remove_endereco2((endereco1))  # Remove o endereço "São Paulo" da lista de endereços
    print(cliente1)  # Exibe as informações do cliente, incluindo seus endereços
