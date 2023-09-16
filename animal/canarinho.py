from ave import Ave


class Canarinho(Ave):
    def __init__(self, tamanho_passo: int, altura_voo: int):
        super().__init__(tamanho_passo, altura_voo)

    def cantar(self):
        return f'{super().produzir_som()} PIU'
