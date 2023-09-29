from tela.livro_tela import LivroTela
from entidade.livro import Livro


class LivroControlador:
    def __init__(self, principal_controlador):
        self.__livros = []
        self.__livro_tela = LivroTela()
        self.__principal_controlador = principal_controlador

    def livros_codigo(self) -> []:
        return [livro.codigo for livro in self.__livros]

    def obter_livro_por_codigo(self, codigo: int) -> Livro:
        for livro in self.__livros:
            if livro.codigo == codigo:
                return livro

    def listar_livros(self):
        if self.__livros:
            self.__livro_tela.lista_livros(self.__livros)
        else:
            self.__livro_tela.mostra_mensagem('Você não tem livros cadastrados!')

    def cadastrar_livro(self):
        dados_livro = self.__livro_tela.obtem_dados_livro()
        if dados_livro['codigo'] in self.livros_codigo():
            self.__livro_tela.mostra_mensagem(f'O livro de código {dados_livro["codigo"]} já existe!')
            return
        novo_livro = Livro(dados_livro['codigo'], dados_livro['titulo'])
        self.__livros.append(novo_livro)
        self.__livro_tela.mostra_mensagem('Livro cadastrado com sucesso!')

    def excluir_livro(self):
        codigo_livro_excluir = self.__livro_tela.obtem_codigo_livro_excluir()
        livro = self.obter_livro_por_codigo(codigo_livro_excluir)
        if livro:
            self.__livros.remove(livro)
            self.__livro_tela.mostra_mensagem('Livro removido com sucesso!')
        else:
            self.__livro_tela.mostra_mensagem('Livro não encontrado...')

    def voltar(self):
        self.__principal_controlador.abrir_menu_principal()

    def abrir_menu_livro(self):
        lista_opcoes = {
            1: self.listar_livros,
            2: self.cadastrar_livro,
            3: self.excluir_livro,
            4: self.voltar,
        }

        while True:
            opcao_escolhida = self.__livro_tela.mostra_menu_livro()
            lista_opcoes[opcao_escolhida]()
