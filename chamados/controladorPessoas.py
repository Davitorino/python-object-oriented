from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self) -> list:
        return self.__clientes

    @property
    def tecnicos(self) -> list:
        return self.__tecnicos

    def __cliente_codigos(self) -> list:
        return [cliente.codigo for cliente in self.__clientes]

    def __tecnico_codigos(self) -> list:
        return [tecnico.codigo for tecnico in self.__tecnicos]

    def inclui_cliente(self, codigo: int, nome: str) -> Cliente:
        if codigo not in self.__cliente_codigos():
            novo_cliente = Cliente(nome, codigo)
            self.__clientes.append(novo_cliente)
            return novo_cliente

    def inclui_tecnico(self, codigo: int, nome: str) -> Tecnico:
        if codigo not in self.__tecnico_codigos():
            novo_tecnico = Tecnico(nome, codigo)
            self.__tecnicos.append(novo_tecnico)
            return novo_tecnico
