"""Factory Method: cada creador concreto decide qué Animal construye."""
from abc import ABC, abstractmethod
from .modelos import Animal, Perro, Gato, FaunaSilvestre, CasoRescate

class CreadorExpediente(ABC):
    @abstractmethod
    def crear_animal(self, nombre: str) -> Animal:
        """Método fábrica que redefinen los creadores concretos."""
        raise NotImplementedError

    def crear_expediente(self, nombre: str, ubicacion: str) -> CasoRescate:
        if not nombre.strip() or not ubicacion.strip():
            raise ValueError("Nombre y ubicación son obligatorios")
        return CasoRescate(self.crear_animal(nombre.strip()), ubicacion.strip())

class CreadorPerro(CreadorExpediente):
    def crear_animal(self, nombre: str) -> Animal:
        return Perro(nombre)

class CreadorGato(CreadorExpediente):
    def crear_animal(self, nombre: str) -> Animal:
        return Gato(nombre)

class CreadorSilvestre(CreadorExpediente):
    def crear_animal(self, nombre: str) -> Animal:
        return FaunaSilvestre(nombre)
