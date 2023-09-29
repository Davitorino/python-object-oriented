from tela.amigo_tela import AmigoTela
from entidade.amigo import Amigo


class AmigoControlador:
    def __init__(self, principal_controlador):
        self.__amigos = []
        self.__amigo_tela = AmigoTela()
        self.__principal_controlador = principal_controlador

    def amigos_cpf(self) -> []:
        return [amigo.cpf for amigo in self.__amigos]

    def obter_amigo_por_cpf(self, cpf: str) -> Amigo:
        for amigo in self.__amigos:
            if amigo.cpf == cpf:
                return amigo

    def listar_amigos(self):
        if self.__amigos:
            self.__amigo_tela.lista_amigos(self.__amigos)
        else:
            self.__amigo_tela.mostra_mensagem('Você não tem amigos cadastrados!')

    def buscar_amigo(self):
        cpf_amigo = self.__amigo_tela.obtem_cpf_amigo_mostrar()
        amigo = self.obter_amigo_por_cpf(cpf_amigo)
        if amigo:
            amigo_livros = self.__principal_controlador.emprestimo_controlador.obter_livros_por_amigo(amigo)
            self.__amigo_tela.mostra_amigo(amigo, amigo_livros)
        else:
            self.__amigo_tela.mostra_mensagem('Amigo não encontrado...')

    def cadastrar_amigo(self):
        dados_amigo = self.__amigo_tela.obtem_dados_amigo_cadastrar()
        if dados_amigo['cpf'] in self.amigos_cpf():
            self.__amigo_tela.mostra_mensagem(f'O amigo de CPF {dados_amigo["cpf"]} já existe!')
            return
        novo_amigo = Amigo(dados_amigo['nome'], dados_amigo['cpf'])
        self.__amigos.append(novo_amigo)
        self.__amigo_tela.mostra_mensagem('Amigo cadastrado com sucesso!')

    def excluir_amigo(self):
        cpf_amigo_excluir = self.__amigo_tela.obtem_cpf_amigo_excluir()
        amigo = self.obter_amigo_por_cpf(cpf_amigo_excluir)
        if amigo:
            self.__amigos.remove(amigo)
            self.__amigo_tela.mostra_mensagem('Amigo removido com sucesso!')
        else:
            self.__amigo_tela.mostra_mensagem('Amigo não encontrado...')

    def editar_amigo(self):
        cpf_amigo_editar = self.__amigo_tela.obtem_cpf_amigo_editar()
        amigo = self.obter_amigo_por_cpf(cpf_amigo_editar)
        if amigo:
            dados_amigo = self.__amigo_tela.obtem_dados_amigo_editar(amigo)
            amigo.nome = dados_amigo['nome']
            amigo.cpf = dados_amigo['cpf']
            self.__amigo_tela.mostra_mensagem('Amigo editado com sucesso!')
        else:
            self.__amigo_tela.mostra_mensagem('Amigo não encontrado...')

    def voltar(self):
        self.__principal_controlador.abrir_menu_principal()

    def abrir_menu_amigo(self):
        lista_opcoes = {
            1: self.listar_amigos,
            2: self.buscar_amigo,
            3: self.cadastrar_amigo,
            4: self.excluir_amigo,
            5: self.editar_amigo,
            6: self.voltar,
        }

        while True:
            opcao_escolhida = self.__amigo_tela.mostra_menu_amigo()
            lista_opcoes[opcao_escolhida]()
