import unittest
from rescate.modelos import Estado, Rol, Responsable, Perro, Gato, FaunaSilvestre
from rescate.fabricas import CreadorPerro, CreadorGato, CreadorSilvestre
from rescate.repositorio import RepositorioMemoria
from rescate.controlador import ControladorRescate
from rescate.notificaciones import (PublicadorCasos, Observador, CorreoAdapter,
                                    ProveedorCorreoSimulado, EventoNuevoCaso)

class PruebasRescate(unittest.TestCase):
    def setUp(self):
        self.repo = RepositorioMemoria()
        self.pub = PublicadorCasos()
        self.correo = ProveedorCorreoSimulado()
        self.pub.suscribir(CorreoAdapter(self.correo, "equipo@example.invalid"))
        self.ctrl = ControladorRescate(self.repo, self.pub)
    def crear(self, creador=None):
        return self.ctrl.registrar(creador or CreadorPerro(), "Luna", "Centro")
    def tratar(self, caso):
        self.ctrl.asignar(caso.id, Responsable("Ana", Rol.VETERINARIO))
        self.ctrl.cambiar_estado(caso.id, Estado.EN_TRATAMIENTO)
    def test_factory_method_crea_tres_productos(self):
        for creador, tipo in [(CreadorPerro(), Perro), (CreadorGato(), Gato),
                               (CreadorSilvestre(), FaunaSilvestre)]:
            with self.subTest(tipo=tipo):
                self.assertIsInstance(self.crear(creador).animal, tipo)
    def test_rechaza_datos_vacios_sin_guardar_ni_notificar(self):
        for nombre, ubicacion in [(" ", "Centro"), ("Luna", " ")]:
            with self.assertRaises(ValueError):
                self.ctrl.registrar(CreadorPerro(), nombre, ubicacion)
        self.assertEqual(self.repo.listar(), [])
        self.assertEqual(self.correo.enviados, [])
    def test_observer_y_adapter_notifican_a_dos_suscriptores(self):
        self.pub.suscribir(CorreoAdapter(self.correo, "vet@example.invalid"))
        caso = self.crear()
        self.assertEqual(len(self.correo.enviados), 2)
        self.assertIn(caso.id, self.correo.enviados[0]["cuerpo"])
    def test_tratamiento_exige_veterinario(self):
        caso = self.crear()
        self.ctrl.asignar(caso.id, Responsable("Luis", Rol.VOLUNTARIO))
        with self.assertRaises(ValueError):
            self.ctrl.cambiar_estado(caso.id, Estado.EN_TRATAMIENTO)
        self.assertEqual(caso.estado, Estado.RESCATADO)
    def test_flujo_domestico_completo_con_historial(self):
        caso = self.crear(); self.tratar(caso)
        self.ctrl.cambiar_estado(caso.id, Estado.EN_ADOPCION)
        self.ctrl.cambiar_estado(caso.id, Estado.ADOPTADO)
        self.assertEqual(caso.estado, Estado.ADOPTADO)
        self.assertIn(Estado.EN_TRATAMIENTO.value, caso.historial)
    def test_fauna_no_adopcion_y_si_derivacion(self):
        caso = self.crear(CreadorSilvestre()); self.tratar(caso)
        with self.assertRaises(ValueError):
            self.ctrl.cambiar_estado(caso.id, Estado.EN_ADOPCION)
        self.ctrl.cambiar_estado(caso.id, Estado.DERIVADO)
        self.assertEqual(caso.estado, Estado.DERIVADO)
    def test_no_permite_salto_de_estados(self):
        caso = self.crear()
        with self.assertRaises(ValueError):
            self.ctrl.cambiar_estado(caso.id, Estado.ADOPTADO)
    def test_asignacion_duplicada_no_duplica_responsable(self):
        caso = self.crear(); r = Responsable("Ana", Rol.VETERINARIO)
        self.ctrl.asignar(caso.id, r); self.ctrl.asignar(caso.id, r)
        self.assertEqual(len(caso.responsables), 1)
    def test_fallo_de_un_observador_no_borra_caso_ni_bloquea_otros(self):
        class ObservadorFallido(Observador):
            def actualizar(self, evento):
                raise RuntimeError("Proveedor no disponible")
        self.pub.suscribir(ObservadorFallido())
        self.pub.suscribir(CorreoAdapter(self.correo, "otro@example.invalid"))
        caso = self.crear()
        self.assertEqual(self.repo.obtener(caso.id), caso)
        self.assertEqual(len(self.ctrl.incidencias_notificacion), 1)
        self.assertEqual(len(self.correo.enviados), 2)
    def test_consulta_inexistente_informa_error(self):
        with self.assertRaisesRegex(ValueError, "Caso no encontrado"):
            self.repo.obtener("inexistente")

if __name__ == "__main__":
    unittest.main()
