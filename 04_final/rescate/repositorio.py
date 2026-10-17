"""Contrato de almacenamiento y adaptador didáctico en memoria."""
from abc import ABC, abstractmethod
from .modelos import CasoRescate

class RepositorioCasos(ABC):
    @abstractmethod
    def guardar(self, caso: CasoRescate) -> None:
        raise NotImplementedError
    @abstractmethod
    def obtener(self, caso_id: str) -> CasoRescate:
        raise NotImplementedError
    @abstractmethod
    def listar(self) -> list[CasoRescate]:
        raise NotImplementedError

class RepositorioMemoria(RepositorioCasos):
    def __init__(self):
        self._casos: dict[str, CasoRescate] = {}
    def guardar(self, caso: CasoRescate) -> None:
        self._casos[caso.id] = caso
    def obtener(self, caso_id: str) -> CasoRescate:
        if caso_id not in self._casos:
            raise ValueError("Caso no encontrado")
        return self._casos[caso_id]
    def listar(self) -> list[CasoRescate]:
        return list(self._casos.values())
