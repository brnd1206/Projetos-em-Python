# Cria classe
class Aluno:
    # Definição de três atributos para a classe
    def __init__(self, nome, mensalidade, idade):
        self.nome = nome
        self.mensalidade = mensalidade
        self.idade = idade

    # Método para retornar os valores dos atributos
    def get_nome(self):
        return self.nome
    def get_mensalidade(self):
        return self.mensalidade
    def get_idade(self):
        return self.idade

    # Método para modificar os valores atribuidos
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def set_mensalidade(self, nova_mensalidade):
        self.mensalidade = nova_mensalidade
    def set_idade(self, nova_idade):
        self.idade = nova_idade

# Função Main para testar a classe
if __name__ == '__main__':
    # Criação de dois objetos da classe ContaBancaria
    aluno1 = Aluno("Paulo", 1100.00, 21)
    aluno2 = Aluno("Emily", 1300.00, 20)

    aluno1.set_mensalidade(nova_mensalidade=1200.00)  # Atualiza a mensalidade de aluno1
    aluno2.set_nome(novo_nome="Alice")  # Atualiza o nome de aluno2
    aluno2.set_idade(nova_idade=21)  # Atualiza a idade de aluno2

    # Mostra os resultados das alterações
    print(f"- Aluno 1: \nNome: {aluno1.get_nome()} \nIdade: {aluno1.get_idade()} \nMensalidade: R${aluno1.get_mensalidade()}")
    print(f"- Aluno 2: \nNome: {aluno2.get_nome()} \nIdade: {aluno2.get_idade()} \nMensalidade: R${aluno2.get_mensalidade()}")
