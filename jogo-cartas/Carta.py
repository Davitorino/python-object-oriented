from AbstractCarta import *
from Personagem import *


class Carta(AbstractCarta):
    def __init__(self, personagem: Personagem):
        self.__personagem = personagem

    def valor_total_carta(self) -> int:
        return self.__personagem.energia + \
            self.__personagem.velocidade + \
            self.__personagem.resistencia + \
            self.__personagem.habilidade

    @property
    def personagem(self) -> Personagem:
        return self.__personagem
