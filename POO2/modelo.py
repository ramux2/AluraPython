class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes
    
    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    def dar_like(self):
        self.likes += 1

    @property
    def likes(self):
        return self.__likes
    
    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


vingadores = Filme("Homem Aranha - Sem volta pra casa", 2022, 160)

vingadores.dar_like()

print(f"Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Like: {vingadores.likes}")

breaking_bad = Serie("Breaking Bad", 2015, 5)

breaking_bad.dar_like()
breaking_bad.dar_like()

print(f"Nome: {breaking_bad.nome} - Ano: {breaking_bad.ano} - Temporadas: {breaking_bad.temporadas} - Likes {breaking_bad.likes}")
