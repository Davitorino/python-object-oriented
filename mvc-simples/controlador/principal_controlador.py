from tela.principal_tela import PrincipalTela
from controlador.amigo_controlador import AmigoControlador
from controlador.livro_controlador import LivroControlador
from controlador.emprestimo_controlador import EmprestimoControlador


class PrincipalControlador:
    def __init__(self):
        self.__principal_tela = PrincipalTela()
        self.__amigo_controlador = AmigoControlador(self)
        self.__livro_controlador = LivroControlador(self)
        self.__emprestimo_controlador = EmprestimoControlador(self)

    @property
    def amigo_controlador(self):
        return self.__amigo_controlador

    @property
    def livro_controlador(self):
        return self.__livro_controlador

    @property
    def emprestimo_controlador(self):
        return self.__emprestimo_controlador

    def iniciar(self):
        self.abrir_menu_principal()

    def sair(self):
        exit(0)

    def abrir_menu_amigo(self):
        self.__amigo_controlador.abrir_menu_amigo()

    def abrir_menu_livro(self):
        self.__livro_controlador.abrir_menu_livro()

    def abrir_menu_emprestimo(self):
        self.__emprestimo_controlador.abrir_menu_emprestimo()

    def abrir_menu_principal(self):
        lista_opcoes = {
            1: self.abrir_menu_amigo,
            2: self.abrir_menu_livro,
            3: self.abrir_menu_emprestimo,
            4: self.sair,
        }

        while True:
            opcao_escolhida = self.__principal_tela.mostra_menu_principal()
            lista_opcoes[opcao_escolhida]()
