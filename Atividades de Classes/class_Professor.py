# Classe base Pessoa que armazena as informações de uma pessoa
class Pessoa:
    # Inicializa a instância com nome e quantidade de dependentes
    def __init__(self, nome="", qtd_dep=0):
        self.nome = nome  # Nome da pessoa
        self.dependente = qtd_dep  # Quantidade de dependentes

    # Método para obter o nome da pessoa
    def get_nome(self):
        return self.nome

    # Método para obter a quantidade de dependentes
    def get_dep(self):
        return self.dependente

    # Método para definir um novo nome, garantindo que seja uma string
    def set_nome(self, novo_nome):
        if type(novo_nome) == str:  # Verifica se o novo nome é uma string
            self.nome = novo_nome  # Atualiza o nome
        else:
            print("Nome inválido!")  # Caso não seja uma string, exibe mensagem de erro

    # Método para definir a quantidade de dependentes
    def set_dep(self, novo_dep):
        self.dependente = novo_dep  # Atualiza a quantidade de dependentes

    # Representação em string da classe Pessoa
    def __str__(self):
        s = (f"Nome: {self.nome}\n"  # Exibe o nome
             f"Quantidade de Dependencia: {self.dependente}\n")  # Exibe a quantidade de dependentes
        return s

# Classe Professor que herda de Pessoa
class Professor(Pessoa):
    # Inicializa a instância com informações específicas de um professor, incluindo nome, dependentes, turma e valor por turma
    def __init__(self, nome="", qtd_dep="", turma="", valor=0):
        super().__init__(nome, qtd_dep)  # Chama o construtor da classe base Pessoa
        self.turma = turma  # Atribui a turma do professor
        self.valor = valor  # Atribui o valor pago por turma

    # Método para obter a turma do professor
    def get_turma(self):
        return self.turma

    # Método para definir uma nova turma, garantindo que seja um valor inteiro maior que 0
    def set_turma(self, nova_turma):
        if nova_turma > 0 and type(nova_turma) == int:  # Verifica se a turma é um número inteiro positivo
            self.turma = nova_turma  # Atualiza a turma
        else:
            print("Valor Inválido!")  # Caso o valor seja inválido, exibe mensagem de erro

    # Método para obter o valor pago por turma
    def get_valor(self):
        return self.valor

    # Método para definir o novo valor pago por turma
    def set_valor(self, novo_valor):
        self.valor = novo_valor  # Atualiza o valor pago por turma

    # Método para calcular o rendimento do professor, que é o valor por turma multiplicado pela quantidade de turmas
    def rendimento(self):
        return self.valor * self.turma

    # Método para calcular o salário total do professor, considerando o rendimento e o bônus por dependente
    def salario_total(self):
        return self.rendimento() + (self.dependente * 100)  # O bônus por dependente é de R$100,00 por dependente

    # Representação em string da classe Professor, mostrando todas as informações relevantes
    def __str__(self):
        s = (f"Nome: {self.nome}\n"  # Exibe o nome do professor
             f"Quantidade de Dependencia: {self.dependente}\n"  # Exibe a quantidade de dependentes
             f"Quantidade de Turma: {self.turma}\n"  # Exibe a quantidade de turmas
             f"Valor por turma: R${self.valor:.2f}\n"  # Exibe o valor pago por turma, formatado para 2 casas decimais
             f"Rendimento: R${self.rendimento():.2f}\n"  # Exibe o rendimento do professor, formatado
             f"Salário Total: R${self.salario_total():.2f}\n")  # Exibe o salário total, formatado
        return s

# Classe Funcionario que herda de Pessoa
class Funcionario(Pessoa):
    # Inicializa a instância com nome, dependentes e salário
    def __init__(self, nome="", qtd_dep=0, salario=0):
        super().__init__(nome, qtd_dep)  # Chama o construtor da classe base Pessoa
        self.salario = salario  # Atribui o salário do funcionário

    # Método para obter o salário do funcionário
    def get_salario(self):
        return self.salario

    # Método para definir o novo salário do funcionário
    def set_salario(self, novo_salario):
        self.salario = novo_salario  # Atualiza o salário

    # Método para calcular o salário total do funcionário, considerando o salário e o bônus por dependente
    def salario_total(self):
        return self.salario + (self.dependente * 100)  # O bônus por dependente é de R$100,00 por dependente

    # Representação em string da classe Funcionario, mostrando todas as informações relevantes
    def __str__(self):
        s = (f"Nome: {self.nome}\n"  # Exibe o nome do funcionário
             f"Quantidade de Dependencia: {self.dependente}\n"  # Exibe a quantidade de dependentes
             f"Salário: R${self.salario_total():.2f}\n")  # Exibe o salário total, formatado
        return s

#Testes
if __name__ == '__main__':
    professor1 = Professor("Arthur", 2, 10, 50)
    print(professor1)
    funcionario1 = Funcionario("Bernardo", 2, 6000)
    print(funcionario1)