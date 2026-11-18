# Plan de exposición: Registro de cuidados por mensaje

Spec: `product/specs/2026-11-17-2300-registro-cuidados.md`

## Hipótesis (de la spec)

Creemos que las personas con más de 15 plantas consultarán la fecha del último riego antes de regar y, al menos a veces, esperarán en vez de regar, porque hoy no recuerdan cuándo regaron cada planta y riegan "por si acaso".
Estamos equivocados si, en una semana, menos de 2 de cada 3 personas consultan la fecha (de una planta con riego registrado) 2 veces o más y esperan al menos una vez por esa fecha.

> Advertencia: la creencia central (#10) no se probó con personas reales; T1 solo se ensayó (synthetic). Ver Preguntas abiertas.

## Secuencia de creencias

1. Las personas registran sus riegos por mensaje sin que nadie se los recuerde (#11). Si no registran, no hay fecha que consultar y el nivel 2 no se puede leer.
2. Con la fecha a mano, las personas consultan antes de regar y a veces esperan (#10, la hipótesis de la spec).
3. Ver el historial de una planta lleva a cambiar cada cuánto la riegan (supuesto de la spec, sin evidencia).

## Nivel 1 — Registrar riegos por mensaje

- **Qué se muestra:** el chat pide la lista de plantas (con apodos), acepta agregar o borrar plantas, y registra riegos ("regué la calathea", varias en un mensaje, "ayer regué…") con confirmación. Sigue oculto: consultar la fecha y el historial.
- **Creencia:** las personas con más de 15 plantas registran sus riegos por mensaje al menos una vez por semana sin recordatorios.
- **Audiencia:** 6 personas con más de 15 plantas que aceptaron conversar en la encuesta y no trabajan con plantas.
- **Duración:** 2 semanas.
- **Validación:** **Avanzar si** al menos 4 de 6 registran al menos un riego en cada una de las 2 semanas. **Detener si** 2 o menos lo hacen: el hábito de registrar no aparece y el resto del plan no se puede leer.

## Nivel 2 — Consultar cuándo regué una planta

- **Qué se muestra:** todo lo del nivel 1, más la consulta "¿cuándo regué la ___?", que responde con la fecha y los días desde el último riego (o "no tengo registrado un riego"), sin consejos. Sigue oculto: el historial.
- **Creencia:** con la fecha a mano, las personas consultan antes de regar y a veces esperan en vez de regar.
- **Audiencia:** las mismas 6 personas del nivel 1.
- **Duración:** 2 semanas.
- **Validación:** **Avanzar si** al menos 4 de 6 consultan una planta con riego registrado 2 veces o más por semana y esperan al menos una vez por la fecha. **Detener si** 2 o menos lo hacen: la fecha no cambia la decisión de regar y la propuesta de valor de A1 no se sostiene.

## Nivel 3 — Historial de una planta

- **Qué se muestra:** todo lo anterior, más "historial de la ___", con los últimos riegos del más reciente al más antiguo.
- **Creencia:** ver el historial de una planta lleva a las personas a cambiar cada cuánto la riegan.
- **Audiencia:** las mismas 6 personas.
- **Duración:** 2 semanas.
- **Validación:** **Avanzar si** al menos 2 de 6 abren el historial de una planta y cuentan un cambio concreto en cómo la riegan (qué planta y qué cambió). **Detener si** nadie abre el historial o nadie cambia nada: el historial no agrega valor y se saca de la spec.

## Mecanismo de exposición

Recomendado: **incremental**. Cada nivel se muestra al mismo grupo completo (no hay subgrupos), y Cami construye sola, nivel por nivel, con el mismo asistente de código. Si más adelante un nivel necesita mostrarse solo a una parte del grupo, conviene pasar a feature flags.

## Validaciones en paralelo

- **Factibilidad del canal (#12):** confirmar el costo y las reglas de operar un chat en WhatsApp (o una alternativa como Telegram) con presupuesto bajo, antes de construir el nivel 1.
- **Precio (#3) y permanencia (#4):** no se prueban con estos niveles; al cerrar el nivel 2, preguntar a quienes consultaron si pagarían ~$1.990 al mes y registrar quién se compromete.
- **Apodos (#13):** en el nivel 1, contar cuántos mensajes el chat no entiende y tiene que preguntar; si son más de 1 de cada 5, revisar cómo se arma la lista antes del nivel 2.

## Preguntas abiertas para el equipo

- **T1 real sigue pendiente.** El concierge por WhatsApp (1 semana, 3 personas) prueba la creencia del nivel 2 sin construir nada. Conviene correrlo antes de construir el nivel 1: si falla, no vale la pena construir.
- **Reclutamiento:** la encuesta dejó 11 personas elegibles con más de 15 plantas. Si se usan 6 en T1 y T2, quedan pocas para los niveles; hace falta sumar un canal fuera de la red de Cami.
- **Tiempos:** los 3 niveles suman 6 semanas, más que lo que queda de la etapa del curso (cierra el 25-11-2026). En esta etapa se puede llegar como mucho al diseño y a T1.
