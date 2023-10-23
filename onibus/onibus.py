from abstractOnibus import AbstractOnibus
from onibusJahCheioException import OnibusJahCheioException
from onibusJahVazioException import OnibusJahVazioException
from onibusJahLigadoException import OnibusJahLigadoException
from onibusJahDesligadoException import OnibusJahDesligadoException


class Onibus(AbstractOnibus):
    def __init__(self, capacidade: int, total_passageiros: int, ligado: bool):
        self.__capacidade = capacidade
        self.__total_passageiros = total_passageiros
        self.__ligado = ligado

    @property
    def capacidade(self) -> int:
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, capacidade):
        self.__capacidade = capacidade

    @property
    def total_passageiros(self) -> int:
        return self.__total_passageiros

    def embarca_pessoa(self) -> str:
        if self.__total_passageiros == self.__capacidade:
            raise OnibusJahCheioException
        self.__total_passageiros += 1

    def desembarca_pessoa(self) -> str:
        if not self.__total_passageiros:
            raise OnibusJahVazioException
        self.__total_passageiros -= 1

    @property
    def ligado(self) -> bool:
        return self.__ligado

    def ligar(self) -> str:
        if self.__ligado:
            raise OnibusJahLigadoException
        self.__ligado = True

    def desligar(self) -> str:
        if not self.__ligado:
            raise OnibusJahDesligadoException
        self.__ligado = False
