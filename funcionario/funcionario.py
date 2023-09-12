from pessoa import Pessoa
from cargo import Cargo
from dependente import Dependente


class Funcionario(Pessoa):
    def __init__(self, nome: str, cpf: str, cargo: Cargo):
        super().__init__(nome, cpf)
        self.__cargo = cargo
        self.__dependentes = []

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo: str):
        self.__cargo = cargo

    @property
    def dependentes(self):
        return self.__dependentes

    def __dependentes_cpfs(self):
        return [dependente.cpf for dependente in self.__dependentes]

    def add_dependente(self, nome: str, cpf: str):
        if cpf not in self.__dependentes_cpfs():
            novo_dependente = Dependente(nome, cpf)
            self.__dependentes.append(novo_dependente)

    def rem_dependente(self, cpf: str):
        if cpf in self.__dependentes_cpfs():
            indice_dependente = self.__dependentes_cpfs().index(cpf)
            self.__dependentes.pop(indice_dependente)

    def mostra_dados(self):
        print('Nome:', self.nome)
        print('CPF:', self.cpf)
        print('Cargo:', self.cargo.descricao)
        print('Dependentes:', ', '.join([dependente.nome for dependente in self.__dependentes]))
