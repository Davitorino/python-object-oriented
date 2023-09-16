from mamifero import Mamifero


class Cachorro(Mamifero):
    def __init__(self):
        super().__init__(3, 3)

    def latir(self):
        return f'{super().produzir_som()} SOM: AU'
