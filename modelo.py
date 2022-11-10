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

class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)
    
    

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
spotify = Serie("Som na Faixa", 2022, 2)
o_irlandes = Filme("o irlândes", 2020, 190)
vikings = Serie("vikings", 2021, 5)

o_irlandes.dar_like()
o_irlandes.dar_like()
o_irlandes.dar_like()
vikings.dar_like()
vingadores.dar_like()
spotify.dar_like()
spotify.dar_like()
spotify.dar_like()



filmes_e_series = [vingadores, spotify, vikings, o_irlandes]

fim_de_semana = Playlist("Fim de Semana", filmes_e_series)

for programa in fim_de_semana:
    print(programa)
