---
name: generate-personas
description: Genera personas del producto (un archivo por persona en product/personas/) a partir de product/overview.md, incluyendo al menos una persona negativa que marca el límite del alcance. Usar cuando se pidan personas, perfiles de usuario o arquetipos del segmento.
---

# generate-personas

Escribe en español. Las personas son hipótesis: salen del overview y de lo que la persona usuaria cuente, no de entrevistas, salvo que existan transcripciones en el repo.

## 1. Leer el contexto

1. Lee `product/overview.md`. Si no existe, detente y sugiere `/start-product`.
2. Revisa si ya hay archivos en `product/personas/` y no los dupliques. Si existe un archivo suelto como `product/personas.md`, propón migrarlo a este formato.
3. Si hay notas de entrevistas o investigación en el repo, úsalas y cita de dónde sale cada dato.

## 2. Decidir el set

- Entre 3 y 5 personas en total.
- Al menos una `primary` (el centro del segmento del overview).
- `secondary` para variaciones que cambian el diseño (otro contexto de uso, otra restricción), no solo otra edad u otro nombre.
- Al menos una `negative`: alguien que parece usuario pero queda fuera a propósito. Explica qué se resolvería mal si se diseñara para esa persona.
- Cada persona debe poner a prueba al menos una creencia del overview. Si una persona no se conecta con ninguna, sobra.

Antes de escribir, muestra la lista (nombre, tipo, una línea) y sigue salvo que la persona usuaria pida cambios.

## 3. Escribir cada archivo

Un archivo por persona: `product/personas/<nombre-apellido>.md`, en minúsculas, con guiones y sin tildes.

```markdown
# <Nombre Apellido>

> "<Cita en primera persona que resuma su relación con el problema.>"

- **Role:** <ocupación y contexto relevante para el producto>
- **Type:** <primary|secondary|negative>
- **Age range:** <ej. 25–34>
- **Location:** <dónde y cómo vive o trabaja, lo relevante>
- **Industry:** <rubro>
- **Technical literacy:** <low|medium|high>
- **Experience level:** <beginner|intermediate|advanced, respecto al dominio del producto>

## Goals

- <2–3 objetivos propios, no del producto.>

## Frustrations

- <2–3 frustraciones concretas, con números o situaciones cuando se pueda.>

## Typical tasks

- <Lo que hace hoy en relación al problema, incluidas las soluciones alternativas que usa.>

## Device preferences

- <Dispositivos y momentos de uso.>

## Creencias que pone a prueba

- <Número y resumen de cada creencia del overview que esta persona valida o refuta.>
```

Para las personas `negative`, reemplaza **Creencias que pone a prueba** por **Por qué queda fuera**.

Reglas:

- Los datos inventados deben ser verosímiles para el país y el mercado del overview (moneda, ciudades, nombres).
- Frustraciones concretas, nada de "le falta tiempo" sin más.
- No describas cómo usaría el producto; describe su vida antes del producto.

## 4. Cerrar

Lista en el chat los archivos creados con una línea por persona. Recuerda que son hipótesis y sugiere cómo reconocer a cada una en entrevistas.
