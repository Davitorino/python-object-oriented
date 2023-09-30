from Carta import *
from AbstractJogador import *
import random


class Jogador(AbstractJogador):
    def __init__(self, nome: str):
        self.__nome = nome
        self.__mao = []

    @property
    def nome(self) -> str:
        return self.__nome

    def baixa_carta_da_mao(self) -> Carta:
        if len(self.__mao):
            indice_carta = random.randint(0, len(self.__mao) - 1)
            return self.__mao.pop(indice_carta)

    @property
    def mao(self) -> list:
        return self.__mao

    def inclui_carta_na_mao(self, carta: Carta):
        self.__mao.append(carta)
