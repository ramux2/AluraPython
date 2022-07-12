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
        return f"{self.nome} - {self.ano} - {self.likes} Likes"


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.duracao} Minutos - {self.likes} Likes"

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.temporadas} Temporadas - {self.likes} Likes"

class Playlist:
        def __init__(self, nome, programas):
            self.nome = nome
            self._programas = programas

        def __getitem__(self, item):
            return self._programas[item]
        
        def __len__(self):
            return len(self._programas)

vingadores = Filme("Homem Aranha - Sem volta pra casa", 2022, 160)
breaking_bad = Serie("Breaking Bad", 2015, 5)
tmep = Filme("todo mundo em pânico", 1999, 99)
vikings = Serie("vikings", 2021, 6)

vingadores.dar_like()
vingadores.dar_like()
tmep.dar_like()
vikings.dar_like()
vikings.dar_like()
vikings.dar_like()
breaking_bad.dar_like()
breaking_bad.dar_like()
breaking_bad.dar_like()

filmes_e_series = [vingadores, breaking_bad, vikings, tmep]

playlist_fim_de_semana = Playlist("fim de semana", filmes_e_series)

print(f"Tamanho da playlist: {len(playlist_fim_de_semana)}")

for programa in playlist_fim_de_semana:
    print(programa)
