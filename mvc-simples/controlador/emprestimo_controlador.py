from tela.emprestimo_tela import EmprestimoTela
from entidade.emprestimo import Emprestimo
from entidade.amigo import Amigo
from entidade.livro import Livro


class EmprestimoControlador:
    def __init__(self, principal_controlador):
        self.__proximo_codigo = 1
        self.__emprestimos = []
        self.__emprestimo_tela = EmprestimoTela()
        self.__principal_controlador = principal_controlador

    def validar_dados_emprestimo(self, amigo: Amigo, livro: Livro) -> bool:
        if not amigo:
            self.__emprestimo_tela.mostra_mensagem('Amigo não encontrado...')
            return False
        if not livro:
            self.__emprestimo_tela.mostra_mensagem('Livro não encontrado...')
            return False
        if livro.emprestado:
            self.__emprestimo_tela.mostra_mensagem('O livro já foi emprestado!')
            return False
        return True

    def obter_emprestimo_por_codigo(self, codigo: int):
        for emprestimo in self.__emprestimos:
            if emprestimo.codigo == codigo:
                return emprestimo

    def obter_livros_por_amigo(self, amigo: Amigo) -> list:
        emprestimos = filter(lambda emprestimo: emprestimo.amigo == amigo, self.__emprestimos)
        return [emprestimo.livro for emprestimo in emprestimos]

    def listar_emprestimos(self):
        if self.__emprestimos:
            self.__emprestimo_tela.lista_emprestimos(self.__emprestimos)
        else:
            self.__emprestimo_tela.mostra_mensagem('Você não tem empréstimos cadastrados!')

    def cadastrar_emprestimo(self):
        dados_emprestimo = self.__emprestimo_tela.obtem_dados_emprestimo()
        amigo = self.__principal_controlador.amigo_controlador.obter_amigo_por_cpf(dados_emprestimo['cpf_amigo'])
        livro = self.__principal_controlador.livro_controlador.obter_livro_por_codigo(dados_emprestimo['codigo_livro'])
        valido = self.validar_dados_emprestimo(amigo, livro)
        if valido:
            novo_emprestimo = Emprestimo(self.__proximo_codigo, amigo, livro)
            self.__emprestimos.append(novo_emprestimo)
            self.__proximo_codigo += 1
            livro.emprestado = True
            self.__emprestimo_tela.mostra_mensagem('Empréstimo cadastrado com sucesso!')

    def excluir_emprestimo(self):
        codigo_emprestimo_excluir = self.__emprestimo_tela.obtem_codigo_emprestimo_excluir()
        emprestimo = self.obter_emprestimo_por_codigo(codigo_emprestimo_excluir)
        if emprestimo:
            self.__emprestimos.remove(emprestimo)
            emprestimo.livro.emprestado = False
            self.__emprestimo_tela.mostra_mensagem('Empréstimo removido com sucesso!')
        else:
            self.__emprestimo_tela.mostra_mensagem('Empréstimo não encontrado...')

    def voltar(self):
        self.__principal_controlador.abrir_menu_principal()

    def abrir_menu_emprestimo(self):
        lista_opcoes = {
            1: self.listar_emprestimos,
            2: self.cadastrar_emprestimo,
            3: self.excluir_emprestimo,
            4: self.voltar,
        }

        while True:
            opcao_escolhida = self.__emprestimo_tela.mostra_menu_emprestimo()
            lista_opcoes[opcao_escolhida]()
