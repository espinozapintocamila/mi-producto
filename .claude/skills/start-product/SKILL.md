---
name: start-product
description: Crea o actualiza product/overview.md, la ficha base del producto (qué es, para quién, creencias no verificadas). Usar al arrancar un producto o caso nuevo, cuando la persona entrega el brief o describe su idea y pide "empezar el producto" o "armar el overview".
---

# start-product

Arma `product/overview.md`, el documento del que dependen todos los demás (personas, entrevistas, specs). Escribe en español.

## 1. Reunir la información

Si `product/overview.md` ya existe, léelo y pregunta qué cambió antes de reescribirlo.

Antes de escribir necesitas saber:

- **Modo:** `new` si es un producto por crear, `existing` si ya existe en el mercado y se trabaja sobre un área.
- **Modelo:** `commercial` (se cobra) u otro (interno, ONG, gratuito).
- **Qué es:** qué hace el producto, en 1–3 frases concretas. Debe incluir lo que la persona ve o hace, no la visión.
- **Para quién:** el segmento, con criterios observables (cantidad, frecuencia, contexto), no adjetivos.
- **Creencias:** lo que tiene que ser cierto para que el producto funcione y aún no se ha comprobado.

Si la persona trae un brief, sácalo de ahí. Pregunta solo lo que falte, en una sola tanda de preguntas.

## 2. Escribir el overview

Usa esta estructura:

```markdown
# <Nombre del producto>

mode: <new|existing> · <commercial|...>

<Qué es, 1–3 frases.>

## Para quién

<Segmento con criterios observables.>

## Creencias no verificadas

Ordenadas por impacto × incertidumbre: la primera es la siguiente a atacar.

1. [<ámbito>] [<riesgo>] <Creencia redactada como afirmación comprobable.>
```

En productos `existing`, si el brief trae más contexto (cómo se vende, cifras, métricas), agrégalo en secciones numeradas antes de las creencias, sin inventar cifras.

Reglas para las creencias:

- **Ámbito:** `[product]`, `[market]` o `[team]`.
- **Riesgo:** `[value]` (¿lo quieren?), `[usability]` (¿pueden usarlo?), `[feasibility]` (¿podemos construirlo?) o `[viability]` (¿funciona como negocio?).
- Cada creencia es una afirmación sobre el mundo que se pueda refutar con evidencia, no una tarea ni una feature.
- Entre 3 y 7 creencias. Ordénalas por impacto × incertidumbre y justifica el orden si no es obvio.

## 3. Cerrar

Resume el overview en el chat en pocas líneas, señala la primera creencia como la siguiente a atacar y sugiere `/generate-personas` como paso siguiente.
