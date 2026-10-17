"""Vista MVC de consola. La validación de estados reside en el modelo."""
from .modelos import CasoRescate

class VistaConsola:
    def mostrar(self, casos: list[CasoRescate]) -> None:
        for caso in casos:
            print(f"{caso.animal.nombre} | {caso.animal.especie} | {caso.estado.value}")
