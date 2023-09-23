from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__tipos_chamados = []
        self.__chamados = []

    @property
    def tipos_chamados(self) -> list:
        return self.__tipos_chamados

    def __tipo_chamado_codigos(self) -> list:
        return [tipo_chamado.codigo for tipo_chamado in self.__tipos_chamados]

    def __chamado_ids(self) -> list:
        return [chamado.identificador for chamado in self.__chamados]

    def inclui_tipochamado(
            self,
            codigo: int,
            nome: str,
            descricao: str) -> TipoChamado:
        if codigo not in self.__tipo_chamado_codigos():
            novo_tipo_chamado = TipoChamado(codigo, descricao, nome)
            self.__tipos_chamados.append(novo_tipo_chamado)
            return novo_tipo_chamado

    def inclui_chamado(
            self,
            data: Date,
            cliente: Cliente,
            tecnico: Tecnico,
            titulo: str,
            descricao: str,
            prioridade: int,
            tipo: TipoChamado) -> Chamado:
        if isinstance(cliente, Cliente) and \
                isinstance(tecnico, Tecnico) and \
                isinstance(tipo, TipoChamado):
            novo_chamado = Chamado(
                data,
                cliente,
                tecnico,
                titulo,
                descricao,
                prioridade,
                tipo
            )
            if novo_chamado.identificador not in self.__chamado_ids():
                self.__chamados.append(novo_chamado)
                return novo_chamado

    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
        chamados = list(filter(
            lambda chamado: chamado.tipo == tipo,
            self.__chamados
        ))
        return len(chamados)
