from pedido_duplicado_exception import PedidoDuplicadoException
from pedido import Pedido


class ControladorPedidos:
    def __init__(self):
        self.__pedidos = []

    @property
    def pedidos(self):
        return self.__pedidos

    def busca_pedido_por_numero(self, numero: int):
        for pedido in self.__pedidos:
            if pedido.numero == numero:
                return pedido

    def incluir_pedido(self, pedido: Pedido):
        if isinstance(pedido, Pedido):
            pedido_existente = self.busca_pedido_por_numero(pedido.numero)
            if pedido_existente:
                raise PedidoDuplicadoException
            self.__pedidos.append(pedido)

    def excluir_pedido(self, numero):
        pedido_existente = self.busca_pedido_por_numero(numero)
        if pedido_existente:
            self.__pedidos.remove(pedido_existente)
            return pedido_existente

    def calcular_faturamento_pedidos(self, distancia: int, cpf: str):
        pedidos_cliente = list(filter(
            lambda pedido: pedido.cliente.cpf == cpf,
            self.__pedidos
        ))
        faturamento_pedidos = sum([pedido.calcula_valor_pedido(distancia)
                                   for pedido
                                   in pedidos_cliente])
        return faturamento_pedidos
