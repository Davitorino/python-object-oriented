from tela.abstract_tela import AbstractTela


class PrincipalTela(AbstractTela):
    def __init__(self):
        pass

    def mostra_menu_principal(self) -> int:
        print('*'*40)
        print('BEM-VINDO À BIBLIOTECA!')
        print('O QUE GOSTARIA DE FAZER?')
        print('*'*40)
        self.mostra_opcoes([
            'Acessar a página de amigos',
            'Acessar a página de livros',
            'Acessar a página de empréstimos',
            'Sair da biblioteca',
        ])
        return self.obtem_opcao([1, 2, 3, 4])
