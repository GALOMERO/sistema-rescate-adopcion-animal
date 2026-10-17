"""Ejecutar desde la raíz: python -m rescate.demo"""
from .modelos import Estado, Responsable, Rol
from .fabricas import CreadorPerro, CreadorGato, CreadorSilvestre
from .repositorio import RepositorioMemoria
from .notificaciones import PublicadorCasos, CorreoAdapter, ProveedorCorreoSimulado
from .controlador import ControladorRescate
from .vista import VistaConsola

def main():
    correo = ProveedorCorreoSimulado()
    publicador = PublicadorCasos()
    publicador.suscribir(CorreoAdapter(correo, "equipo@example.invalid"))
    controlador = ControladorRescate(RepositorioMemoria(), publicador)
    perro = controlador.registrar(CreadorPerro(), "Luna", "Sector norte")
    controlador.registrar(CreadorGato(), "Milo", "Sector centro")
    silvestre = controlador.registrar(CreadorSilvestre(), "Ave rescatada", "Sector rural")
    veterinaria = Responsable("Dra. Ana", Rol.VETERINARIO)
    controlador.asignar(perro.id, Responsable("Luis", Rol.VOLUNTARIO))
    controlador.asignar(perro.id, veterinaria)
    controlador.cambiar_estado(perro.id, Estado.EN_TRATAMIENTO)
    controlador.cambiar_estado(perro.id, Estado.EN_ADOPCION)
    controlador.cambiar_estado(perro.id, Estado.ADOPTADO)
    controlador.asignar(silvestre.id, veterinaria)
    controlador.cambiar_estado(silvestre.id, Estado.EN_TRATAMIENTO)
    controlador.cambiar_estado(silvestre.id, Estado.DERIVADO)
    VistaConsola().mostrar(controlador.listar())
    print(f"Notificaciones simuladas: {len(correo.enviados)}")
    print(f"Incidencias de notificación: {len(controlador.incidencias_notificacion)}")

if __name__ == "__main__":
    main()
