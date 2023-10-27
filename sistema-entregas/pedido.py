from cliente import Cliente
from tipo_pedido import TipoPedido
from item_pedido import ItemPedido
from cliente_fidelidade import ClienteFidelidade


class Pedido:
    def __init__(self, numero: int, cliente: Cliente, tipo: TipoPedido):
        self.__numero = numero
        self.__cliente = cliente
        self.__tipo = tipo
        self.__itens = []

    @property
    def numero(self):
        return self.__numero

    @property
    def cliente(self):
        return self.__cliente

    @property
    def tipo(self):
        return self.__tipo

    @property
    def itens(self):
        return self.__itens

    @numero.setter
    def numero(self, numero: int):
        self.__numero = numero

    @cliente.setter
    def cliente(self, cliente: Cliente):
        self.__cliente = cliente

    @tipo.setter
    def tipo(self, tipo: TipoPedido):
        self.__tipo = tipo

    def busca_item_por_codigo(self, codigo: int):
        for item in self.__itens:
            if item.codigo == codigo:
                return item

    def inclui_item_pedido(self, codigo, descricao, preco):
        item_existente = self.busca_item_por_codigo(codigo)
        if not item_existente:
            novo_item = ItemPedido(codigo, descricao, preco)
            self.__itens.append(novo_item)
            return novo_item

    def exclui_item_pedido(self, codigo):
        item_existente = self.busca_item_por_codigo(codigo)
        if item_existente:
            self.__itens.remove(item_existente)
            return item_existente

    def calcula_valor_pedido(self, distancia: float):
        valor_itens = sum([item.preco_unitario for item in self.__itens])
        adicional_distancia = distancia * self.__tipo.fator_distancia
        percentual_total = 1
        if isinstance(self.__cliente, ClienteFidelidade):
            percentual_total -= self.__cliente.desconto
        valor_total = (valor_itens + adicional_distancia) * percentual_total
        return valor_total
