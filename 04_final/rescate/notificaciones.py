"""Observer y Adapter. El proveedor simulado no envía correos reales."""
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass(frozen=True)
class EventoNuevoCaso:
    caso_id: str
    especie: str
    ubicacion: str

class Observador(ABC):
    @abstractmethod
    def actualizar(self, evento: EventoNuevoCaso) -> None:
        raise NotImplementedError

class PublicadorCasos:
    def __init__(self):
        self._observadores: list[Observador] = []
    def suscribir(self, observador: Observador) -> None:
        if observador not in self._observadores:
            self._observadores.append(observador)
    def publicar(self, evento: EventoNuevoCaso) -> list[str]:
        errores = []
        for observador in self._observadores:
            try:
                observador.actualizar(evento)
            except Exception as exc:
                errores.append(f"{type(observador).__name__}: {exc}")
        return errores

class ServicioCorreo(ABC):
    @abstractmethod
    def enviar(self, destino: str, asunto: str, cuerpo: str) -> None:
        raise NotImplementedError

class ProveedorCorreoSimulado(ServicioCorreo):
    def __init__(self):
        self.enviados: list[dict[str, str]] = []
    def enviar(self, destino: str, asunto: str, cuerpo: str) -> None:
        self.enviados.append({"destino": destino, "asunto": asunto, "cuerpo": cuerpo})

class CorreoAdapter(Observador):
    def __init__(self, servicio: ServicioCorreo, destino: str):
        self._servicio, self._destino = servicio, destino
    def actualizar(self, evento: EventoNuevoCaso) -> None:
        self._servicio.enviar(
            self._destino, "Nuevo rescate",
            f"Caso {evento.caso_id}: {evento.especie} en {evento.ubicacion}",
        )
