---
source: secondary
method: web
date: 2026-10-21
question: ¿Qué apps de plantas permiten compartir el registro entre varias personas de un hogar, y cómo lo cobran (por persona, por hogar o gratis)?
opportunity: coordinacion-riego
---

# Research: apps de plantas con registro compartido

Compartir el cuidado de plantas **ya existe** en el mercado, con dos enfoques opuestos: Planta lo ofrece **solo en premium** (invitar a familiares o a quien cuida las plantas), mientras que apps nuevas y pequeñas como Potally y Roomers lo dan **gratis** y lo usan como su propuesta central ("regado por Sarah hace 3 días"). Para cobrar por hogar hay un mecanismo estándar: Apple permite que el desarrollador ofrezca un plan familiar a un solo precio para todo el grupo. La pregunta abierta deja de ser "¿se puede cobrar por hogar?" y pasa a ser "¿por qué pagaría un hogar si hay alternativas gratis?".

## Competidores directos

| App | Cómo comparte | Precio de compartir | Tracción | Fuente |
|---|---|---|---|---|
| Planta | Invitar "familiares" (pueden agregar, quitar y editar plantas) o "plant sitters" (solo marcan tareas hechas) | Invitar requiere premium; no dice si el invitado también paga (desconocido) | App grande y establecida | [verificado: support.getplanta.com, actualizado 2026-03-09 — 2026-10-21] |
| Potally | "Espacios" compartidos por código o correo, sincronización en tiempo real, cada registro dice quién lo hizo; para roommates, parejas y familias | Gratis; no menciona compras dentro de la app | desconocido | [verificado: apps.apple.com/us/app/potally/id6753342763 — 2026-10-21] |
| Roomers | Un registro compartido sincronizado entre los teléfonos de quienes viven juntos, para no regar dos veces | Gratis, sin compras dentro de la app (según su creador) | Lanzada en 2026; 7 votos y 11 seguidores en Product Hunt | [verificado: producthunt.com/products/roomers-plants-for-roommates — 2026-10-21] |
| Greg | No se encontró información sobre compartir | desconocido | — | — |

**Lo que prueba su existencia:** otras personas vieron el mismo problema que `coordinacion-riego` ("regar dos veces", "quién regó") y lo convirtieron en producto. **Lo que no prueba:** que los hogares del segmento sufran el problema lo suficiente, ni que paguen por resolverlo. Roomers tiene muy poca tracción, así que su existencia no es evidencia de demanda.

## Alternativas y no consumo

- Turnos anotados en papel o en el refrigerador, grupos de WhatsApp de la casa [conocimiento del modelo — verificar]. Son las alternativas que aparecen en la persona sintética de Daniela; no hay datos.

## Precios y modelos de negocio

- **Compartir como premium** (Planta): se usa como una razón más para pagar.
- **Compartir gratis** (Potally, Roomers): es la propuesta central; no se ve cómo ganan plata (desconocido).
- **Plan familiar de Apple:** el desarrollador decide si lo ofrece, y un solo plan cubre a todo el grupo. Ejemplo de Macworld: USD 24,99 al año el plan familiar frente a USD 14,99 el individual, unas 1,7 veces [verificado: macworld.com, artículo de 2021-05-31 — 2026-10-21]. Es un ejemplo, no un estándar de precios.

## Posicionamiento

- "Quién regó y cuándo" ya es el mensaje de Potally y Roomers: no es un espacio vacío.
- Planta distingue roles (familiar que edita vs. plant sitter que solo marca), lo que sugiere que no todas las personas del hogar se involucran igual [verificado: support.getplanta.com].

## Impacto en creencias

| Creencia (de overview.md) | Veredicto | Evidencia |
|---|---|---|
| #5 [opportunity: coordinacion-riego] [value] En hogares compartidos se riega dos veces o nadie riega, y eso les ha costado plantas | no dice nada | Potally y Roomers describen ese problema, pero es lo que dicen sus creadores, no evidencia de usuarios; Roomers tiene muy poca tracción. |
| #6 [opportunity: coordinacion-riego] [usability] Todas las personas del hogar registrarían cada riego | no dice nada (señal débil en contra) | Planta crea un rol "plant sitter" con menos permisos: sugiere que no todos se involucran igual [verificado: support.getplanta.com]. No hay datos de uso. |
| #7 [opportunity: coordinacion-riego] [viability] Un hogar pagaría una sola suscripción compartida y el negocio sigue funcionando | apoya el modelo, contradice el qué | Cobrar por hogar es posible y tiene un mecanismo estándar (plan familiar de Apple) [verificado: macworld.com]. Pero hay apps que comparten gratis [verificado: App Store, Product Hunt], y Planta lo usa como un extra del premium, no como lo único que cobra. |
| #3 [product] [viability] Pagarían ~$1.990 al mes | no dice nada nuevo | — |

## Qué sigue necesitando research primario

- **Entrevistas** (`/design-interview`), a las dos personas del hogar por separado: ¿se han pisado con el riego? ¿les ha costado plantas? (#5); ¿la persona que no es "la de las plantas" registraría cada riego? (#6).
- **Encuesta** (`/design-survey`): cuántos hogares del segmento tienen a más de una persona regando (#5), y si pagarían por un plan para el hogar vs. por persona (#7).
- Desconocido: si Planta cobra a cada persona invitada, y cómo ganan plata Potally y Roomers.
