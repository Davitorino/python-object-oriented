

class Livro:
    def __init__(self, codigo: int, titulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__emprestado = False

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: int):
        self.__titulo = titulo

    @property
    def emprestado(self):
        return self.__emprestado

    @emprestado.setter
    def emprestado(self, emprestado: bool):
        self.__emprestado = emprestado
