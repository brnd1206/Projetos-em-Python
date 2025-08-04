class Pessoa:
    # Construtor da classe Pessoa
    def __init__(self, nome, peso, altura, ano_nasc):
        # Inicializa os atributos da pessoa com os valores fornecidos
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.ano_nasc = ano_nasc

    # Método para obter o nome da pessoa
    def get_nome(self):
        return self.nome

    # Método para obter o peso da pessoa
    def get_peso(self):
        return self.peso

    # Método para obter a altura da pessoa
    def get_altura(self):
        return self.altura

    # Método para obter o ano de nascimento da pessoa
    def get_ano_nasc(self):
        return self.ano_nasc

    # Método para definir um novo nome para a pessoa
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    # Método para definir um novo peso para a pessoa
    def set_peso(self, novo_peso):
        self.peso = novo_peso

    # Método para definir uma nova altura para a pessoa
    def set_altura(self, nova_altura):
        # Corrigido: Atribuição direta ao invés de chamada de método
        self.altura = nova_altura

    # Método para definir um novo ano de nascimento para a pessoa
    def set_ano_nasc(self, novo_ano):
        # Verifica se o novo ano é um número inteiro
        if type(novo_ano) == int:
            self.ano_nasc = novo_ano
        else:
            print("Erro: tipo inválido")  # Exibe uma mensagem de erro se o tipo for inválido

    # Método para calcular o Índice de Massa Corporal (IMC)
    def calculo_imc(self):
        # Retorna o valor do IMC usando a fórmula peso / altura^2
        return self.peso / (self.altura ** 2)

if __name__ == '__main__':
    # Cria uma instância da classe Pessoa com dados iniciais
    pessoa1 = Pessoa("Bernardo", 50, 1.90, 2006)
    pessoa2 = Pessoa("Hugo", 80, 1.99, 1999)

    # Atualiza o nome e o peso da primeira pessoa
    pessoa1.set_nome("André")
    pessoa1.set_peso(100)

    # Exibe informações sobre a primeira pessoa, incluindo o nome, ano de nascimento e IMC
    print("Nome:", pessoa1.get_nome(),
          "\nAno Nascimento:", pessoa1.get_ano_nasc(),
          "\nIMC:", pessoa1.calculo_imc())