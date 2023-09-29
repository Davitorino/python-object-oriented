from tela.abstract_tela import AbstractTela


class EmprestimoTela(AbstractTela):
    def __init__(self):
        pass

    def mostra_menu_emprestimo(self) -> int:
        self.mostra_titulo('EMPRÉSTIMOS')
        self.mostra_opcoes([
            'Listar emprestimos',
            'Cadastrar novo emprestimo',
            'Excluir emprestimo',
            'Voltar para o menu principal',
        ])
        return self.obtem_opcao([1, 2, 3, 4])

    def lista_emprestimos(self, emprestimos: []):
        self.mostra_titulo('EMPRÉSTIMOS')
        print('\n'.join(
            [
                f'{emprestimo.codigo} - Livro: {emprestimo.livro.titulo} - Amigo: {emprestimo.amigo.nome}'
                for emprestimo in emprestimos
            ]
        ))

    def obtem_dados_emprestimo(self) -> dict:
        self.mostra_titulo('CADASTRO DE EMPRÉSTIMO')
        cpf_amigo = input('Digite o CPF do amigo: ')
        while True:
            try:
                codigo_livro = int(input('Digite o código (número) do livro: '))
                return {'cpf_amigo': cpf_amigo, 'codigo_livro': codigo_livro}
            except ValueError:
                print('O código do livro deve ser um número!')

    def obtem_codigo_emprestimo_excluir(self):
        self.mostra_titulo('EXCLUSAO DE EMPRÉSTIMO')
        print('Qual empréstimo deseja excluir?')
        while True:
            try:
                return int(input('Digite o código do empréstimo: '))
            except ValueError:
                print('O código do empréstimo deve ser um número!')
