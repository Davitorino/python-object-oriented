

class Cargo:
    def __init__(self, salario: float, descricao: str):
        self.__salario = salario
        self.__descricao = descricao

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario: float):
        self.__salario = salario

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao
