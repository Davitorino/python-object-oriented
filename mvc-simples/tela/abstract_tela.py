from abc import ABC, abstractmethod


class AbstractTela(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def mostra_opcoes(self, opcoes: []):
        for index, opcao in enumerate(opcoes, start=1):
            print(f'{index} - {opcao}')

    def obtem_opcao(self, opcoes_validas: [] = None) -> int:
        while True:
            try:
                opcao = int(input('Selecione uma opção: '))
                if opcoes_validas and opcao not in opcoes_validas:
                    raise ValueError
                return opcao
            except ValueError:
                print('Selecione uma opção válida!')

    def mostra_titulo(self, secao: str):
        print(f'{"*"*12} {secao} {"*"*12}')

    def mostra_mensagem(self, mensagem: str):
        print(mensagem)
