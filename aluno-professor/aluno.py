from pessoa import Pessoa
from professor import Professor


class Aluno(Pessoa):

    def __init__(self, matricula: int, nome: str, endereco: str, orientador: Professor):
        super().__init__(nome, endereco)
        if isinstance(matricula, int):
            self.__matricula = matricula
        if isinstance(orientador, Professor):
            self.__orientador = orientador

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula: int):
        if isinstance(matricula, int):
            self.__matricula = matricula

    @property
    def orientador(self):
        return self.__orientador

    @orientador.setter
    def orientador(self, orientador: Professor):
        if isinstance(orientador, Professor):
            self.__orientador = orientador
