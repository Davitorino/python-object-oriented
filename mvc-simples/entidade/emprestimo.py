from entidade.amigo import Amigo
from entidade.livro import Livro


class Emprestimo:
    def __init__(self, codigo: int, amigo: Amigo, livro: Livro):
        self.__codigo = codigo
        self.__amigo = amigo
        self.__livro = livro

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def amigo(self) -> int:
        return self.__amigo

    @amigo.setter
    def amigo(self, amigo: int):
        self.__amigo = amigo

    @property
    def livro(self):
        return self.__livro

    @livro.setter
    def livro(self, livro: int):
        self.__livro = livro
