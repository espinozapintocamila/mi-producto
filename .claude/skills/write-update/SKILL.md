---
name: write-update
description: Redacta un update del trabajo de producto para una persona de la empresa que construye el producto (CEO, Legal, Marketing, Ingeniería…), a partir de lo guardado en product/ — qué creíamos, qué aprendimos, qué decidimos y qué pedimos. Úsala cuando se pida escribir un update, un reporte de avance o un mensaje a un stakeholder sobre el producto.
argument-hint: "[audiencia, p. ej. CEO]"
---

# /write-update

Redacta un update del trabajo de producto para **una** persona de la empresa que construye el producto. Escribe para quien lo lee: lo que necesita para decidir, no todo lo que se hizo.

Entrada: $ARGUMENTS

## 1. Leer

Lee en `product/`, antes de preguntar, para que las opciones salgan de ahí:

| Qué | Dónde |
|---|---|
| Overview | `product/overview.md` |
| Oportunidad | `product/opportunities/` |
| Pruebas de solución | `product/tests/` |
| Spec | `product/specs/` |
| Plan de exposición | `product/exposure-plans/` |
| Análisis de métricas y de feedback | `product/insights/*-metrics-*.md` y `product/insights/*-feedback-*.md` |

- Parte de la spec más reciente y sigue sus enlaces a la oportunidad, las pruebas y el plan. Si hay varias specs u oportunidades sin enlace entre sí, pregunta cuál.
- Si algo no existe, omítelo. No lo reemplaces con otra cosa ni lo supongas.
- Un archivo de `product/metrics/` define qué se va a medir: no es un resultado.
- Si no existe `product/` o está vacía, dilo y detente.

## 2. Preguntar

Una pregunta por vez, y espera la respuesta antes de hacer la siguiente. Cada una con 2 a 4 opciones de ejemplo sacadas de lo leído, más la opción de escribir la propia. Usa la herramienta de preguntas si está disponible. Salta lo que ya venga respondido en los argumentos.

1. **Para quién es** el update, y qué decisión toma o qué le preocupa.
2. **Qué se le va a pedir:** una decisión, un recurso, una aprobación o nada. Si hay pedido y no quedó claro qué es o para cuándo, pregunta eso antes de seguir.
3. **Qué largo.** Por defecto, que se lea en dos minutos: no más de 250 palabras.

## 3. Redactar

Cuatro partes, en este orden:

1. **Qué creíamos:** la apuesta, en una o dos líneas.
2. **Qué aprendimos:** los resultados que le importan a esa persona, con números cuando los hay, diciendo si cada dato es real o sintético.
3. **Qué decidimos:** qué hacemos ahora y por qué.
4. **Qué pedimos:** un pedido concreto, con plazo. Si no hay pedido, dilo: "No necesito nada de ti por ahora".

Reglas:

- **No inventa datos.** Todo número y toda decisión sale de un archivo leído. Si en los archivos no hay una decisión o un resultado, dilo en vez de completarlo.
- **No maquilla.** Si algo no funcionó, no se hizo o quedó como ensayo, lo dice, y dice qué se hace con eso. Si eso no está decidido, lo dice también.
- **Real o sintético, dato por dato.** Respeta la procedencia del archivo (`real`, `survey`, `synthetic`, `secondary`, `unverified`) y dila en palabras simples: "con personas reales", "ensayo con respuestas inventadas", "dato sin fuente". Un resultado sintético nunca se presenta como aprendizaje sobre los usuarios. Con pocas personas, di cuántas fueron ("2 de 3", no "67%").
- **Sin jerga del equipo sin explicar.** Nada de códigos (T1, A1, #10) ni términos del método (`weakened`, concierge, nivel 1) sin decir qué significan.
- **Sin datos personales** de usuarios o participantes.
- **En el idioma de la conversación.**

## 4. Revisar

Antes de mostrarlo, comprueba:

- Cada número está en un archivo leído y coincide con él.
- Cada dato dice si es real o sintético.
- El largo: cuenta las palabras con código, no a ojo. Si se pasa, corta lo que no ayuda a decidir; nunca el resultado malo ni la procedencia.
- El pedido tiene plazo, o dice que no hay pedido.

## 5. Mostrar, esperar el OK y guardar

- Muestra el **borrador completo** en la conversación. Debajo, fuera del borrador: la cantidad de palabras, de qué archivo sale cada dato, y qué no existía y se omitió.
- **No guardes nada hasta tener el OK.** Si piden cambios, muestra de nuevo el borrador completo.
- Con el OK, guarda solo el update en `product/comms/{YYYY-MM-DD}-{audiencia}.md`, con la fecha del día y la audiencia en minúsculas y sin acentos (p. ej. `2026-11-25-ceo.md`). Si ese archivo ya existe, no lo sobrescribas: agrega la hora (`2026-11-25-1830-ceo.md`).
- No envíes el update, no hagas commit y no cambies ningún otro archivo de `product/`, salvo que te lo pidan.
