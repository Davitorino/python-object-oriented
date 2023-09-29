from tela.abstract_tela import AbstractTela
from entidade.amigo import Amigo


class AmigoTela(AbstractTela):
    def __init__(self):
        pass

    def mostra_menu_amigo(self) -> int:
        self.mostra_titulo('AMIGOS')
        self.mostra_opcoes([
            'Listar amigos',
            'Buscar amigo',
            'Cadastrar novo amigo',
            'Excluir amigo',
            'Editar amigo',
            'Voltar para o menu principal',
        ])
        return self.obtem_opcao([1, 2, 3, 4, 5, 6])

    def obtem_cpf(self) -> str:
        return input('Digite o CPF do amigo: ')

    def obtem_dados_amigo(self) -> dict:
        nome = input('Digite o nome do seu amigo: ')
        cpf = input('Digite o CPF do seu amigo: ')
        return {'nome': nome, 'cpf': cpf}

    def lista_amigos(self, amigos: []):
        self.mostra_titulo('AMIGOS')
        print('\n'.join([f'{amigo.nome} - CPF: {amigo.cpf}' for amigo in amigos]))

    def mostra_amigo(self, amigo: Amigo, livros: []):
        self.mostra_titulo('AMIGO')
        print(f'{amigo.nome} - CPF: {amigo.cpf}')
        print('Livros emprestados:')
        for livro in livros:
            print(f'{livro.titulo} - Código: {livro.codigo}')

    def obtem_cpf_amigo_mostrar(self):
        self.mostra_titulo('BUSCAR AMIGO')
        print('Quem deseja buscar?')
        return self.obtem_cpf()

    def obtem_dados_amigo_cadastrar(self) -> dict:
        self.mostra_titulo('CADASTRO DE AMIGO')
        return self.obtem_dados_amigo()

    def obtem_cpf_amigo_editar(self) -> str:
        self.mostra_titulo('EDIÇÃO DE AMIGO')
        print('Quem deseja editar?')
        return self.obtem_cpf()

    def obtem_dados_amigo_editar(self, amigo: Amigo) -> dict:
        print(f'{amigo.nome} - CPF: {amigo.cpf}')
        return self.obtem_dados_amigo()

    def obtem_cpf_amigo_excluir(self) -> str:
        self.mostra_titulo('EXCLUSAO DE AMIGO')
        print('Quem deseja excluir?')
        return self.obtem_cpf()
