class Ejemplo:
    def __init__(self, peso: int, altura: int) -> None:

        self.peso = peso
        self.altura = altura

    def dame_resultados(self) -> None:
        """_summary_"""
        print(self.peso, self.altura)
