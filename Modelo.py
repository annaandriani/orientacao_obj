class Programa:                         #classe mãe, vai passar os atributos para as subclasses
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._like = 0

    @property
    def like(self):
        return self._like

    def dar_like(self):
        self._like += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f' {self._nome} - {self.ano}: {self._like}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome} - ano {self.ano} - {self.duracao} min - {self._like} likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    def __str__(self):
        return f'Nome: {self._nome} - ano {self.ano} - {self.temporadas} min - {self._like} likes'

class playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)


Atlanta = Serie('atlanta', 2018, 2)
Vingadores = Filme('Vingadores - guerra infinita', 2018, 160)
sorte_no_amor = Filme('sorte no amor', 2014, 100)
tqi = Filme('Te quiero imbécil', 2020, 180)

Vingadores.dar_like()
Vingadores.dar_like()
Vingadores.dar_like()
Atlanta.dar_like()
Atlanta.dar_like()
sorte_no_amor.dar_like()
sorte_no_amor.dar_like()
sorte_no_amor.dar_like()
sorte_no_amor.dar_like()
sorte_no_amor.dar_like()
tqi.dar_like()
tqi.dar_like()
tqi.dar_like()
tqi.dar_like()

filmes_e_series = [Vingadores, Atlanta, sorte_no_amor, tqi]
fim_de_semana = playlist('fim de semana', filmes_e_series)
print(f'tamanho da playlist: {len(fim_de_semana)}')

for Programa in fim_de_semana:  #polimorfismo, a partir da classe mãe, é possível correr um FOR sem se preocupar com o tipo contido
    print(Programa)
#MIXIN compartilhamento de algum comportamento que não é o mais importante da classe.