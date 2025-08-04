#Cria a classe
class ContaBancaria:
    #Definição de quatro atributos para a classe
    def __init__(self, titular, saldo, numero_conta, agencia):
        self.titular = titular
        self.saldo = saldo
        self.numero_conta = numero_conta
        self.agencia = agencia

    #Método para retornar os valores dos atributos
    def get_titular(self):
        return self.titular
    def get_saldo(self):
        return self.saldo
    def get_numero_conta(self):
        return self.numero_conta
    def get_agencia(self):
        return self.agencia

    #Método para modificar os valores atribuidos.
    def set_titular(self, novo_titular):
        self.titular = novo_titular
    def set_saldo(self, novo_saldo):
        if novo_saldo >= 0:
            self.saldo = novo_saldo
        else:
            print("O saldo não pode ser negativo")
    def set_numero_conta(self, novo_numero_conta):
        self.numero_conta = novo_numero_conta
    def set_agencia(self, nova_agencia):
        self.agencia = nova_agencia

    #Método mostra dados usando diretamente os atributos
    def mostra_dados(self):
        return (f"Titular: {self.titular}\n"
                f"Saldo: R${self.saldo:.2f}\n"
                f"Número da Conta: {self.numero_conta}\n"
                f"Agência: {self.agencia}")

    #Método mostra dados usando os getters
    def mostra_dados_get(self):
        return (f"Titular: {self.get_titular()}\n"
                f"Saldo: R${self.get_saldo():.2f}\n"
                f"Número da Conta: {self.get_numero_conta()}\n"
                f"Agência: {self.get_agencia()}")

    #Método retorna todos os atributos
    def retorna_dados(self):
        return {
            "titular": self.get_titular(),
            "saldo:": self.get_saldo(),
            "numero_conta": self.get_numero_conta(),
            "agencia": self.get_agencia()
        }

#Função Main para testar a classe
if __name__ == '__main__':
    #Criação de três objetos da classe ContaBancaria
    conta1 = ContaBancaria("Alice", 1000, "123456", "0001")
    conta2 = ContaBancaria("Bob", 500, "654321", "0002")
    conta3 = ContaBancaria("Carlos", 1500, "789012", "0003")

    #Testando métodos da classe:
    #Através de atributos
    print("Dados da conta 1:")
    print(conta1.mostra_dados())
    #Através de métodos get
    print("\nDados da conta 1:")
    print(conta1.mostra_dados_get())
    #Dados retornados
    print("\nDados retornados da conta 1:")
    print(conta1.retorna_dados())

    #Modificando alguns atributos usando setters
    conta1.set_titular("João")
    conta1.set_saldo(1200)
    conta1.set_numero_conta("1234567")
    conta1.set_agencia("0002")

    #Testando as modificações:
    #Através de atributos
    print("\nDados atualizados da conta 1:\n")
    print(conta1.mostra_dados())
    #Através de métodos get
    print("\nDados atualizados da conta 1:")
    print(conta1.mostra_dados_get())
    #Dados retornados
    print("\nDados retornados da conta 1 atualizados:")
    print(conta1.retorna_dados())