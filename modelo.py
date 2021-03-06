# Código referente à segunda parte do Curso de Orientação à Objetos

class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes




class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes


vingadores = Filme('Vingadores - Guerra Infinita', 2018, 160)
vingadores.dar_like()
vingadores.dar_like()
print(f"Nome: {vingadores.nome} - ano: {vingadores.ano} - Temporadas: {vingadores.duracao} - Likes:{vingadores.likes}")

atlanta = Serie('Atlanta', 2018, 2)
atlanta.dar_like()
print(f"Nome: {atlanta.nome} - ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}")
