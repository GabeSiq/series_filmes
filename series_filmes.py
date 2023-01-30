#Programa para listagem de PROGRAMAS - Filmes e Series por meio da orientação de objetos.
class Programa: #define-se o nome/ano de lançam,ento
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self): #possibilita dar likes dentro de cada um dos objetos criados para um futuro ranqueamento
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome): #possibilita acessar o nome e altera-lo
        self._nome = novo_nome.title()

    def __str__(self): #retorna os objetos formatados e o numero de likes
        return f'{self._nome} - {self.ano} - {self._likes} Likes'

#A partir daqui o programa se divide em filme e serie
class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'


class Playlist: #função monta playlists dos programas gerados
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self): #lista os programas
        return self._programas

    def __len__(self):
        return len(self._programas)

    def __getitem__(self, item):
        return self._programas[item]


#Testes

vingadores = Filme('vingadores - guerra infinita', 2018, 180)
atlanta = Serie('atlanta', 2017, 2)
acasadodragao = Serie('a casa do dragão', 2022, 1)
tmep = Filme('Todo mundo em panico', 2016, 100)
