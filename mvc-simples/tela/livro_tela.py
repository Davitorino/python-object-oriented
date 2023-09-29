from tela.abstract_tela import AbstractTela


class LivroTela(AbstractTela):
    def __init__(self):
        pass

    def mostra_menu_livro(self) -> int:
        self.mostra_titulo('LIVROS')
        self.mostra_opcoes([
            'Listar livros',
            'Cadastrar novo livro',
            'Excluir livro',
            'Voltar para o menu principal',
        ])
        return self.obtem_opcao([1, 2, 3, 4])

    def lista_livros(self, livros: []):
        self.mostra_titulo('LIVROS')
        print('\n'.join(
            [f'{livro.titulo} - Código: {livro.codigo}{" (E)" if livro.emprestado else ""}' for livro in livros]
        ))

    def obtem_dados_livro(self) -> dict:
        self.mostra_titulo('CADASTRO DE LIVRO')
        titulo = input('Digite o título do livro: ')
        while True:
            try:
                codigo = int(input('Digite o código (número) do livro: '))
                return {'titulo': titulo, 'codigo': codigo}
            except ValueError:
                print('O código do livro deve ser um número!')

    def obtem_codigo_livro_excluir(self) -> int:
        self.mostra_titulo('EXCLUSAO DE LIVRO')
        print('Qual livro deseja excluir?')
        while True:
            try:
                return int(input('Digite o código do livro: '))
            except ValueError:
                print('O código do livro deve ser um número!')
