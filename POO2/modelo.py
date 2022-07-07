class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0
    
    def dar_like(self):
        self.like += 1

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0

    def dar_like(self):
        self.like += 1


vingadores = Filme("Homem Aranha - Sem volta pra casa", 2022, 160)

vingadores.dar_like()

print(f"Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Like: {vingadores.likes}")

breaking_bad = Serie("Breaking Bad", 2015, 5)

breaking_bad.dar_like()
breaking_bad.dar_like()

print(f"Nome: {breaking_bad.nome} - Ano: {breaking_bad.ano} - Temporadas: {breaking_bad.temporadas} - Likes {breaking_bad.likes}")
