from AbstractControladorJogo import *
import random


class ControladorJogo(AbstractControladorJogo):
    def __init__(self):
        self.__baralho = []
        self.__personagens = []

    @property
    def baralho(self) -> list:
        return self.__baralho

    @property
    def personagems(self) -> list:
        return self.__personagens

    def inclui_personagem_na_lista(self,
                                   energia: int,
                                   habilidade: int,
                                   velocidade: int,
                                   resistencia: int,
                                   tipo: Tipo) -> Personagem:
        novo_personagem = Personagem(energia, habilidade,
                                     velocidade, resistencia, tipo)
        self.__personagens.append(novo_personagem)
        return novo_personagem

    def inclui_carta_no_baralho(self, personagem: Personagem) -> Carta:
        nova_carta = Carta(personagem)
        self.__baralho.append(nova_carta)
        return nova_carta

    def jogada(self, mesa: Mesa) -> Jogador:
        carta_jogador1 = mesa.carta_jogador1
        carta_jogador2 = mesa.carta_jogador2
        diff = carta_jogador1.valor_total_carta() - \
            carta_jogador2.valor_total_carta()

        if diff == 0:
            mesa.jogador1.inclui_carta_na_mao(carta_jogador1)
            mesa.jogador2.inclui_carta_na_mao(carta_jogador2)
            return

        vencedor, perdedor = (mesa.jogador1, mesa.jogador2) \
            if diff > 0 else (mesa.jogador2, mesa.jogador1)
        vencedor.inclui_carta_na_mao(carta_jogador1)
        vencedor.inclui_carta_na_mao(carta_jogador2)

        if len(perdedor.mao) == 0:
            return vencedor
