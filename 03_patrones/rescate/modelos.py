"""Entidades y reglas del refugio. No dependen de la interfaz ni del correo."""
from dataclasses import dataclass, field
from enum import Enum
from uuid import uuid4

class Estado(str, Enum):
    RESCATADO = "Rescatado"
    EN_TRATAMIENTO = "En tratamiento"
    EN_ADOPCION = "En adopción"
    ADOPTADO = "Adoptado"
    DERIVADO = "Derivado a autoridad competente"

class Rol(str, Enum):
    VOLUNTARIO = "Voluntario"
    VETERINARIO = "Veterinario"

@dataclass(frozen=True)
class Responsable:
    nombre: str
    rol: Rol

@dataclass(frozen=True)
class Animal:
    nombre: str
    especie: str

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "Perro")

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "Gato")

class FaunaSilvestre(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "Fauna silvestre")

@dataclass
class CasoRescate:
    animal: Animal
    ubicacion: str
    id: str = field(default_factory=lambda: str(uuid4()))
    estado: Estado = Estado.RESCATADO
    responsables: list[Responsable] = field(default_factory=list)
    historial: list[str] = field(default_factory=lambda: [Estado.RESCATADO.value])

    def asignar(self, responsable: Responsable) -> None:
        if not responsable.nombre.strip() or not isinstance(responsable.rol, Rol):
            raise ValueError("El responsable requiere nombre y rol válido")
        if responsable not in self.responsables:
            self.responsables.append(responsable)
            self.historial.append(f"Asignación: {responsable.rol.value} {responsable.nombre}")

    def cambiar_estado(self, nuevo: Estado) -> None:
        permitidos = {
            Estado.RESCATADO: {Estado.EN_TRATAMIENTO},
            Estado.EN_TRATAMIENTO: {Estado.EN_ADOPCION, Estado.DERIVADO},
            Estado.EN_ADOPCION: {Estado.ADOPTADO},
            Estado.ADOPTADO: set(), Estado.DERIVADO: set(),
        }
        if nuevo not in permitidos[self.estado]:
            raise ValueError("Transición de estado no permitida")
        es_silvestre = isinstance(self.animal, FaunaSilvestre)
        if es_silvestre and nuevo in {Estado.EN_ADOPCION, Estado.ADOPTADO}:
            raise ValueError("La fauna silvestre no ingresa en adopción doméstica")
        if not es_silvestre and nuevo == Estado.DERIVADO:
            raise ValueError("Esta derivación corresponde a fauna silvestre")
        if nuevo == Estado.EN_TRATAMIENTO and not any(
            r.rol == Rol.VETERINARIO for r in self.responsables
        ):
            raise ValueError("Asigne un veterinario antes del tratamiento")
        self.estado = nuevo
        self.historial.append(nuevo.value)
