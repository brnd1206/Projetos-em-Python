# Cria classe
class Produto:
    # Definição de quatro atributos para a classe
    def __init__(self, nome, valor, quantidade, codigo):
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade
        self.codigo = codigo

    # Método para retornar os valores dos atributos
    def get_nome(self):
        return self.nome
    def get_valor(self):
        return self.valor
    def get_quantidade(self):
        return self.quantidade
    def get_codigo(self):
        return self.codigo

    # Método para modificar os valores atribuidos
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def set_valor(self, novo_valor):
        if novo_valor > 0:
            self.valor = novo_valor
        else:
            print("O valor não pode ser negativo.")
    def set_quantidade(self, novo_quantidade):
        self.quantidade = novo_quantidade
    def set_codigo(self, novo_codigo):
        if novo_codigo > 0:
            self.valor = novo_codigo
        else:
            print("O valor não pode ser negativo.")

    # Método mostra dados usando diretamente os atributos
    def mostra_dados(self):
        return (f"Nome: {self.nome}\n"
                f"Preço: R${self.valor:.2f}\n"
                f"Quantidade: {self.quantidade}\n"
                f"Código: {self.codigo}")

    # Método mostra dados usando os getters
    def mostra_dados_get(self):
        return (f"Nome: {self.get_nome()}\n"
                f"Preço: R${self.get_valor:.2f}\n"
                f"Quantidade: {self.get_quantidade}\n"
                f"Código: {self.get_codigo}")

    # Método retorna todos os atributos
    def retorna_dados(self):
        return {
            "nome:": self.get_nome(),
            "preço:": self.get_valor(),
            "quantidade": self.get_quantidade(),
            "código": self.get_codigo()
        }

    # Método para somar o valor digitado ao valor original
    def aumenta_valor(self, aumenta_valor):
        self.valor = self.valor + aumenta_valor

if __name__ == '__main__':
    produto1 = Produto("Produto A", 50, 10, 101)
    produto2 = Produto("Produto B", 25.5, 20, 102)
    produto3 = Produto("Produto C", 30, 15, 103)

    # Mostrando dados usando o método mostra_dados
    print("Dados do Produto 1:")
    print(produto1.mostra_dados())

    print("\nDados do Produto 2:")
    print(produto2.mostra_dados())

    print("\nDados do Produto 3:")
    print(produto3.mostra_dados())

    # Usando o método aumenta_valor para aumentar o preço do produto1 em R$10
    produto1.aumenta_valor(10)

    # Mostrando dados após aumento do preço
    print("\nDados do Produto 1 após aumento de 10% no preço:")
    print(produto1.mostra_dados())

    # Usando os métodos retorna_dados
    print("\nRetornando dados do Produto 2:")
    print(produto2.retorna_dados())