from abstractControladorOnibus import AbstractControladorOnibus
from comandoInvalidoException import ComandoInvalidoException
from onibus import Onibus


class ControladorOnibus(AbstractControladorOnibus):
    def __init__(self):
        self.__onibus = None

    @property
    def onibus(self) -> Onibus:
        return self.__onibus

    def inicializar_onibus(self,
                           capacidade: int,
                           total_passageiros: int,
                           ligado: bool):
        if isinstance(capacidade, int) and \
                isinstance(total_passageiros, int) and \
                isinstance(ligado, bool) and \
                capacidade >= 0 and \
                0 <= total_passageiros <= capacidade and \
                ligado:
            self.__onibus = Onibus(capacidade, total_passageiros, ligado)
            return
        raise ComandoInvalidoException

    def ligar(self) -> str:
        self.__onibus.ligar()

    def desligar(self) -> str:
        self.__onibus.desligar()

    def embarca_pessoa(self) -> str:
        self.__onibus.embarca_pessoa()

    def desembarca_pessoa(self) -> str:
        self.__onibus.desembarca_pessoa()
