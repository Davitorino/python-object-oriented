from pessoa import Pessoa


class Professor(Pessoa):

    def __init__(self, id_funcionario: int, nome: str, endereco: str, telefone: str):
        super().__init__(nome, endereco)
        if isinstance(id_funcionario, int):
            self.__id_funcionario = id_funcionario
        if isinstance(telefone, str):
            self.__telefone = telefone

    @property
    def id_funcionario(self):
        return self.__id_funcionario

    @id_funcionario.setter
    def id_funcionario(self, id_funcionario: int):
        if isinstance(id_funcionario, int):
            self.__id_funcionario = id_funcionario

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        if isinstance(telefone, str):
            self.__telefone = telefone
