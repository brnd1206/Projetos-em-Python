class Jogo:
    def __init__(self, nome, plataforma, valor=0):
        # Inicializa os atributos do jogo
        self.nome = nome
        self.plataforma = plataforma
        self.valor = valor

    def get_nome(self):
        # Retorna o nome do jogo
        return self.nome
    def get_plataforma(self):
        # Retorna a plataforma do jogo
        return self.plataforma
    def get_valor(self):
        # Retorna o valor do jogo
        return self.valor

    def set_nome(self, novo_nome):
        # Atualiza o nome do jogo
        self.nome = novo_nome
    def set_plataforma(self, nova_plataforma):
        # Atualiza a plataforma do jogo
        self.plataforma = nova_plataforma
    def set_valor(self, novo_valor):
        # Atualiza o valor do jogo, apenas se for maior que zero
        if novo_valor > 0:
            self.valor = novo_valor
        else:
            print("Valor inválido! O valor deve ser maior que zero.")

    def aumenta_valor(self, aumento):
        # Aumenta o valor do jogo
        self.valor += aumento

    def __str__(self):
        # Representação em string do objeto Jogo
        s = (f"Nome: {self.nome}\n"
             f"Plataforma: {self.plataforma}\n"
             f"Preço: R${self.valor:.2f}\n")
        return s

class JogoDeRpg(Jogo):
    def __init__(self, nome, plataforma, mapa, valor=0):
        # Inicializa os atributos da subclasse JogoDeRpg
        super().__init__(nome, plataforma, valor)
        self.mapa = mapa
        self.progresso = 0

    def get_mapa(self):
        # Retorna o mapa do jogo
        return self.mapa
    def get_progresso(self):
        # Retorna o progresso do jogo
        return self.progresso

    def set_mapa(self, mapa):
        # Atualiza o mapa do jogo
        self.mapa = mapa
    def set_progresso(self, progresso):
        # Atualiza o progresso, validando o valor
        if progresso < 0 or progresso > 100:
            raise ValueError("O progresso deve ser entre 0 e 100.")
        self.progresso = progresso

    def explorar(self):
        # Simula a exploração, aumentando o progresso
        self.progresso += 10
        if self.progresso > 100:
            self.progresso = 100
        print(f"Explorando o mapa de {self.mapa}. Progresso: {self.progresso}%.")

class JogoDeEstrategia(Jogo):
    def __init__(self, nome, plataforma, exercitos=0, recurso_principal="Ouro", valor=0):
        # Inicializa os atributos da subclasse JogoDeEstrategia
        super().__init__(nome, plataforma, valor)
        self.exercitos = exercitos
        self.recurso_principal = recurso_principal

    def get_exercitos(self):
        # Retorna o número de exércitos
        return self.exercitos
    def get_recurso_principal(self):
        # Retorna o recurso principal do jogo
        return self.recurso_principal

    def set_exercitos(self, exercitos):
        # Atualiza o número de exércitos, validando o valor
        if exercitos < 0:
            raise ValueError("O número de exércitos não pode ser negativo.")
        self.exercitos = exercitos
    def set_recurso_principal(self, recurso_principal):
        # Atualiza o recurso principal
        self.recurso_principal = recurso_principal

    def recrutar_exercito(self):
        # Recruta um novo exército, aumentando o total
        self.exercitos += 1
        print(f"Um novo exército foi recrutado! Total de exércitos: {self.exercitos}.")

if __name__ == '__main__':
    # Criando objetos das classes
    jogo1 = Jogo("Super Mario", "Nintendo Switch", 199.99)
    jogo2 = JogoDeRpg("Zelda: Breath of the Wild", "Nintendo Switch", "Hyrule", 299.99)
    jogo3 = JogoDeEstrategia("Age of Empires", "PC", 5, "Madeira", 199.99)

    # Testando os métodos da superclasse Jogo
    print(jogo1)
    jogo1.set_valor(89.99)
    print("Valor atualizado:", jogo1.get_valor())
    jogo1.aumenta_valor(10)
    print("Valor após aumento:", jogo1.get_valor())

    # Testando os métodos da subclasse JogoDeRpg
    print(jogo2)
    jogo2.explorar()
    jogo2.set_progresso(50)
    print("Progresso atualizado:", jogo2.get_progresso())

    # Testando a validação do progresso
    try:
        jogo2.set_progresso(110)  # Isso deve gerar um erro
    except ValueError as e:
        print(e)

    # Testando os métodos da subclasse JogoDeEstrategia
    print(jogo3)
    jogo3.recrutar_exercito()
    print("Exércitos após recrutamento:", jogo3.get_exercitos())
    jogo3.set_exercitos(10)
    print("Exércitos atualizados:", jogo3.get_exercitos())

    # Testando a validação do número de exércitos
    try:
        jogo3.set_exercitos(-1)  # Isso deve gerar um erro
    except ValueError as e:
        print(e)