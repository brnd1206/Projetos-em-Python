# Classe Cliente representa um cliente com CPF e nome.
class Cliente:
    # Método construtor, inicializa CPF e nome com valores padrão (0 e "")
    def __init__(self, cpf=0, nome=""):
        self.cpf = cpf
        self.nome = nome

    # Método para obter o CPF do cliente
    def get_cpf(self):
        return self.cpf

    # Método para alterar o CPF do cliente
    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf

    # Método para obter o nome do cliente
    def get_nome(self):
        return self.nome

    # Método para alterar o nome do cliente
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    # Método para representar o cliente em formato de string (para visualização)
    def __str__(self):
        return (f"CPF: {self.cpf}\n"
                f"Nome: {self.nome}\n")


# Classe Produto representa um produto comprado, com ID, nome, preço e quantidade.
class Produto:
    # Método construtor, inicializa o produto com ID, nome, preço e quantidade.
    def __init__(self, id_produto, nome_produto, preco=0.0, qtd_comprada=1):
        self.id_produto = id_produto
        self.nome_produto = nome_produto
        self.preco = preco
        self.qtd_comprada = qtd_comprada

    # Método para obter o ID do produto
    def get_id(self):
        return self.id_produto

    # Método para alterar o ID do produto
    def set_id(self, nova_id):
        self.id_produto = nova_id

    # Método para obter o nome do produto
    def get_nome_produto(self):
        return self.nome_produto

    # Método para alterar o nome do produto
    def set_nome_produto(self, novo_nome):
        self.nome_produto = novo_nome

    # Método para obter o preço do produto
    def get_preco(self):
        return self.preco

    # Método para alterar o preço do produto
    def set_preco(self, novo_preco):
        self.preco = novo_preco

    # Método para obter a quantidade comprada do produto
    def get_qtd(self):
        return self.qtd_comprada

    # Método para alterar a quantidade comprada do produto
    def set_qtd(self, nova_qtd):
        self.qtd_comprada = nova_qtd

    # Método para representar o produto em formato de string (para visualização)
    def __str__(self):
        return (f"ID: {self.id_produto}\n"
                f"NOME: {self.nome_produto}\n"
                f"PREÇO: R${self.preco:.2f}\n"
                f"QUANTIDADE: {self.qtd_comprada}\n")


# Classe CarrinhoCompra representa um carrinho de compras de um cliente.
class CarrinhoCompra:
    # Método construtor, inicializa o carrinho com número do pedido e cliente associado
    def __init__(self, n_pedido, o_cliente):
        self.n_pedido = n_pedido
        self.o_cliente = o_cliente
        self.l_produtos = []  # Lista que irá armazenar os produtos no carrinho

    # Método para obter o número do pedido
    def get_n_pedidos(self):
        return self.n_pedido

    # Método para alterar o número do pedido
    def set_n_pedidos(self, n_pedido2):
        self.n_pedido = n_pedido2

    # Método para obter o cliente do carrinho
    def get_cliente(self):
        return self.o_cliente

    # Método para alterar o cliente do carrinho
    def set_cliente(self, novo_cliente):
        self.o_cliente = novo_cliente

    # Método para mostrar o nome do cliente
    def mostra_nome_cliente(self):
        return self.o_cliente.get_nome()

    # Método para adicionar um produto ao carrinho
    def insere_produto(self, produto):
        self.l_produtos.append(produto)  # Adiciona o produto à lista de produtos
        print(f"{produto.get_nome_produto()} adicionado com sucesso!")

    # Método para remover um produto do carrinho (se encontrado)
    def remove_produto(self, produto):
        self.l_produtos.remove(produto)  # Remove o produto da lista

    # Método para remover um produto com verificação de erros (ex.: carrinho vazio ou produto não encontrado)
    def remove_produto2(self, produto):
        if len(self.l_produtos) == 0:
            print("O carrinho está vazio. Não há produtos para remover.")
        elif produto not in self.l_produtos:
            print(f"{produto.get_nome_produto()} não está no carrinho. Não foi possível removê-lo.")
        else:
            self.l_produtos.remove(produto)  # Remove o produto da lista
            print(f"{produto.get_nome_produto()} removido com sucesso!")

    # Método para exibir os nomes dos produtos no carrinho
    def mostra_carrinho(self):
        if len(self.l_produtos) == 0:
            return "Carrinho Vazio"  # Caso o carrinho esteja vazio
        for produto in self.l_produtos:
            print(produto.get_nome_produto())  # Exibe o nome de cada produto

    # Método para exibir os detalhes completos dos produtos no carrinho
    def mostra_carrinho2(self):
        if len(self.l_produtos) == 0:
            return "Carrinho Vazio"  # Caso o carrinho esteja vazio
        for produto in self.l_produtos:
            print(produto)  # Exibe os detalhes completos do produto

    # Método para calcular o valor total da compra (somando os preços dos produtos)
    def calcula_total(self):
        total = 0
        for produto in self.l_produtos:
            total += produto.get_preco() * produto.get_qtd()  # Preço * Quantidade
        return total

    # Método para finalizar a compra e exibir um resumo
    def fecha_compra(self):
        if len(self.l_produtos) == 0:
            print("O carrinho está vazio. Não é possível finalizar a compra.")  # Caso o carrinho esteja vazio
        else:
            print(f"Compra finalizada com sucesso! Pedido nº {self.n_pedido}\n")

#Testes
if __name__ == '__main__':
    cliente1 = Cliente(106, "Guilherme")
    carrinho1 = CarrinhoCompra(12, cliente1)
    produto1 = Produto(1, "Bola", 60, 2)
    produto2 = Produto(2, "Chuteira", 600, 1)
    produto3 = Produto(3, "Uniforme", 300, 10)
    carrinho1.insere_produto(produto1)
    carrinho1.insere_produto(produto2)
    carrinho1.insere_produto(produto3)
    carrinho1.remove_produto2(produto3)
    carrinho1.fecha_compra()