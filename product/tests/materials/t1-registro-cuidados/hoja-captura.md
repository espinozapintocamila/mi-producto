# T1 · Hoja de captura

Se llena con los IDs de la encuesta (R-13…), no con nombres ni teléfonos.

## Por persona

| Persona | Origen | Más de 15 plantas | Motivo de la última planta ahogada (día 0) |
|---|---|---|---|
| R-13 | real (opt-in de la encuesta) | sí | |
| R-31 | real (opt-in de la encuesta) | sí | |
| R-36 | real (opt-in de la encuesta) | sí | |

## Por evento (una fila cada vez que avisan o consultan)

| Persona | Fecha y hora | Tipo (aviso de riego / consulta) | Planta | Si es consulta: días desde el último riego que les diste | Qué hizo después (regó / esperó / no respondió) | Demora de tu respuesta |
|---|---|---|---|---|---|---|
| | | | | | | |

## Resumen al día 7

| Persona | Avisos de riego | Consultas | Veces que esperó por la fecha | Respuestas del cierre |
|---|---|---|---|---|
| R-13 | | | | |
| R-31 | | | | |
| R-36 | | | | |

## Cómo se lee (fijo, no se cambia después de correr la prueba)

- Una persona **cuenta** si tiene **2 o más consultas** y al menos **1 vez esperó** por la fecha.
- **Pasa** si cuentan **2 de 3**.
- **Change** si avisan sus riegos, pero tienen **menos de 2 consultas**.
- **Discard** si cuentan **1 o ninguna**.
- Si una persona abandona antes del día 4, se reemplaza (R-17, R-04, R-08). Si no hay reemplazo, su resultado es `inconclusive`.
