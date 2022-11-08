class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self.ano} Likes: {self.likes}"

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self.ano} - Duracao: {self.duracao} min - Likes: {self.likes}"
    

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self.ano} - Temporadas: {self.temporadas} Temporadas - Likes: {self.likes}"

class Playlist(Filme, Serie):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano, duracao)
    pass

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
vingadores.dar_like()


spotify = Serie("Som na Faixa", 2022, 2)
spotify.dar_like()
spotify.dar_like()
spotify.dar_like()



filmes_e_series = [vingadores, spotify]

for programa in filmes_e_series:
    print(programa)
