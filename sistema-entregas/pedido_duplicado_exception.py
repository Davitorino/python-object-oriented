

class PedidoDuplicadoException(Exception):
    def __init__(self):
        super().__init__('O pedido está duplicado!')
