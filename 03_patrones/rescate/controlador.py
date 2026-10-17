"""Controlador MVC con dependencias recibidas por constructor."""
from .fabricas import CreadorExpediente
from .modelos import CasoRescate, Responsable, Estado
from .repositorio import RepositorioCasos
from .notificaciones import PublicadorCasos, EventoNuevoCaso

class ControladorRescate:
    def __init__(self, repositorio: RepositorioCasos, publicador: PublicadorCasos):
        self._repositorio, self._publicador = repositorio, publicador
        self.incidencias_notificacion: list[str] = []
    def registrar(self, creador: CreadorExpediente, nombre: str, ubicacion: str) -> CasoRescate:
        caso = creador.crear_expediente(nombre, ubicacion)
        self._repositorio.guardar(caso)
        evento = EventoNuevoCaso(caso.id, caso.animal.especie, caso.ubicacion)
        self.incidencias_notificacion.extend(self._publicador.publicar(evento))
        return caso
    def asignar(self, caso_id: str, responsable: Responsable) -> None:
        caso = self._repositorio.obtener(caso_id)
        caso.asignar(responsable)
        self._repositorio.guardar(caso)
    def cambiar_estado(self, caso_id: str, nuevo: Estado) -> None:
        caso = self._repositorio.obtener(caso_id)
        caso.cambiar_estado(nuevo)
        self._repositorio.guardar(caso)
    def listar(self) -> list[CasoRescate]:
        return self._repositorio.listar()
