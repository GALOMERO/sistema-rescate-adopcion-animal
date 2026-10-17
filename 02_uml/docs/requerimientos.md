# Análisis del sistema

## Alcance y actores
Ciudadano/reportante, voluntario, veterinario y administrador del refugio.
Se registran perros, gatos y fauna silvestre; las salidas son adopción doméstica o derivación de fauna.

## Requerimientos funcionales y criterios de aceptación
- **RF01** Registrar un rescate con nombre del animal y ubicación.
- **RF02** Clasificar perro, gato o fauna silvestre y crear su expediente.
- **RF03** Asignar voluntarios y veterinarios a cada caso.
- **RF04** Actualizar estados y conservar el historial del caso.
- **RF05** Notificar nuevos rescates a los suscriptores del refugio.
- **RF06** Consultar casos y cerrar por adopción o derivación de fauna.

## Reglas de aceptación
- El nombre del animal y la ubicación no pueden estar vacíos.
- Los creadores concretos producen Perro, Gato y FaunaSilvestre.
- Se asignan responsables con rol Voluntario o Veterinario y nombre válido.
- El tratamiento requiere al menos un veterinario asignado.
- Los cambios de estado respetan la transición y se agregan al historial.
- La fauna silvestre no entra en adopción; se deriva desde tratamiento.
- El evento de nuevo caso llega a todos los suscriptores.
- Si falla una notificación, se conserva el caso y se registra la incidencia.

## Requerimientos no funcionales propuestos
- Mantenibilidad: separar dominio, creación, eventos, vista y almacenamiento.
- Extensibilidad: ampliar especies y canales respetando los contratos.
- Escalabilidad prevista: sustituir almacenamiento y notificaciones por servicios adecuados al crecimiento, sin afirmar un rendimiento no medido.
- Trazabilidad: historial del caso y cambios del proyecto en Git.
- Protección de datos: acceso por roles, autenticación y datos mínimos en una futura aplicación.

## Límites del prototipo
El código verifica las reglas y los patrones principales con datos en memoria. No implementa una interfaz web, autenticación, permisos de cada sesión, base de datos, historia clínica completa ni envío real de correo. Las restricciones por actor del diagrama de casos de uso corresponden al diseño de la futura aplicación.
