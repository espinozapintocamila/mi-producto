# Registro de cuidados por mensaje

## Problema

Las personas con muchas plantas de interior no recuerdan cuándo regaron cada una. Cuando dudan, riegan "por si acaso" y las ahogan: en el segmento de más de 15 plantas, 10 de 12 perdieron plantas en el último año, 5 de 10 por regar de más, y 7 de 12 no sabían cuándo habían regado todas la última vez que regaron. Casi nadie lleva un registro (28 de 31 nunca anotaron nada), así que la duda se resuelve tocando la tierra o a ojo. Importa ahora porque la etapa del curso cierra el 25-11-2026 y esta es la alternativa que sigue en prueba.

> Evidencia: "He matado más plantas por sobre-riego que por sequía" — R-25 (16 a 30 plantas), `product/insights/2026-11-03-2117-encuesta-olvido-riego.md`
> Evidencia: Q3 en el segmento — "de algunas sí y de otras no" 6, "de ninguna" 1, "sí, de todas" 5 (n=12, survey)

## Para quién

Carolina Vidal (primary): tiene 22 plantas, riega de noche "a ojo" y no sabe cuáles regó hace 3 días y cuáles hace 2 semanas. Usa WhatsApp a diario y descarga pocas apps, por eso el registro vive en un chat y no en una app nueva.

## Recorrido

1. **Disparador:** de noche, después del trabajo, Carolina ve una planta y duda si la regó el fin de semana o no (persona carolina-vidal, synthetic; Q3 de la encuesta, survey).
2. Le escribe al chat: "¿cuándo regué la calathea?".
3. El chat le responde: "La regaste el sábado 14, hace 3 días."
4. Toca la tierra como siempre (8 de 12 deciden así; survey) y, con la fecha, decide esperar.
5. El domingo riega varias plantas y escribe: "regué la calathea, el potus y la monstera". El chat confirma.
6. **Resultado:** la próxima vez que duda, tiene la fecha a mano y no riega "por si acaso". Es el paso donde llega el valor (paso 4).

Los pasos 1 a 5 combinan la persona sintética con lo que mostró la encuesta; el paso 4 es justamente lo que T1 tiene que probar.

## Historias críticas

### Registrar un riego con un mensaje

Como Carolina, quiero avisar en un mensaje qué plantas regué, para no tener que anotarlo en ningún otro lado.

Criterios de aceptación:
- [ ] Un mensaje con una planta ("regué la calathea") queda registrado con fecha y hora, y el chat lo confirma.
- [ ] Un mensaje con varias plantas ("regué la calathea, el potus y la monstera") registra cada una por separado.
- [ ] "Ayer regué el potus" queda registrado con la fecha de ayer.
- [ ] Si el nombre no corresponde a ninguna planta de su lista, el chat pregunta cuál es en vez de inventar una.
- [ ] Si dos plantas tienen nombres parecidos ("potus grande" y "potus chico"), el chat pregunta cuál.

Se basa en: `product/solutions/2026-11-03-2124-olvido-riego.md` (A1); `product/tests/2026-11-10-1928-olvido-riego.md` (T1, paso 2)

### Consultar cuándo regué una planta

Como Carolina, quiero preguntar cuándo regué una planta, para decidir si la riego o espero.

Criterios de aceptación:
- [ ] "¿Cuándo regué la calathea?" se responde con la fecha y los días que pasaron desde el último riego.
- [ ] Si la planta no tiene riegos registrados, el chat lo dice ("No tengo registrado un riego de esa planta") y no inventa una fecha.
- [ ] La respuesta no incluye consejos de cuánta agua dar ni si conviene regar.
- [ ] La respuesta llega en menos de 1 minuto.

Se basa en: `product/tests/2026-11-10-1928-olvido-riego.md` (T1, paso 3); Q3 de la encuesta

### Armar mi lista de plantas

Como Carolina, quiero decirle al chat qué plantas tengo con los nombres que yo uso, para que entienda cuando le hablo de "la calathea del living".

Criterios de aceptación:
- [ ] Al empezar, el chat pide la lista de plantas y acepta apodos libres.
- [ ] Puede agregar o borrar una planta después con un mensaje ("agrega la sansevieria", "borra el ficus").
- [ ] Con 22 plantas o más, la lista se guarda completa.

Se basa en: `product/tests/2026-11-10-1928-olvido-riego.md` (T1, día 0)

### Ver el historial de una planta

Como Carolina, quiero ver los últimos riegos de una planta, para entender cada cuánto la estoy regando.

Criterios de aceptación:
- [ ] "Historial de la calathea" muestra los últimos riegos con fecha, del más reciente al más antiguo.
- [ ] Si tiene menos de dos riegos, lo dice en vez de mostrar una lista vacía.

Se basa en: `product/solutions/2026-11-03-2124-olvido-riego.md` (A1: ficha por planta con historial). Supuesto: la encuesta no muestra que lo pidan.

## Hipótesis

Creemos que las personas con más de 15 plantas consultarán la fecha del último riego antes de regar y, al menos a veces, esperarán en vez de regar, porque hoy no recuerdan cuándo regaron cada planta y riegan "por si acaso".
Estamos equivocados si, en una semana, menos de 2 de cada 3 personas consultan la fecha (de una planta con riego registrado) 2 veces o más y esperan al menos una vez por esa fecha.

## Alternativas consideradas

Exploradas en: `product/solutions/2026-11-03-2124-olvido-riego.md`
- A2 Guía de riego por planta — en prueba en paralelo (T2), no descartada
- A3 Etiqueta en la maceta — parked: la más barata y sirve en hogares compartidos; vuelve si se retoma `coordinacion-riego`
- A4 Medidor de humedad — parked: modelo de negocio distinto (hardware)

## Probado antes de la spec

Probado en: `product/tests/2026-11-10-1928-olvido-riego.md`
- T1 Fecha del último riego por WhatsApp — passed solo como ensayo (synthetic, 3 respuestas ficticias) · #10. **La prueba real no se corrió: riskiest belief not tested (declared).**
- T2 Tarjetas por planta (A2, no esta spec) — failed solo como ensayo (synthetic).

## Supuestos

- [product] [value] Las personas del target no recuerdan cuándo regaron por última vez cada planta, y eso les ha costado plantas secas o ahogadas. (#1 — weakened solo en lo de plantas secas)
- [product] [viability] Pagarían alrededor de $1.990 CLP al mes por una app que les lleve este registro. (#3)
- [opportunity: olvido-riego] [viability] Quienes paguen la suscripción seguirán usándola y pagándola después de 3 meses, porque registrar un riego les toma menos esfuerzo que el que les costó su Excel o sus notas. (#4)
- [feature: registro-cuidados] [value] Las personas con más de 15 plantas que ahogaron plantas regaron sin saber si ya las habían regado, y con la fecha del último riego a la vista riegan de más menos veces en las 4 semanas siguientes. (#10 — sin probar con personas reales)
- [feature: registro-cuidados] [usability] Las personas con más de 15 plantas registrarán al menos un riego por semana durante 4 semanas, aunque nunca han anotado nada. (#11)
- [feature: registro-cuidados] [feasibility] El registro por mensaje se puede operar en un canal de chat (por ejemplo WhatsApp) con el presupuesto y el tiempo de una sola persona. (#12 — dueña: Cami, que es quien construye)
- [feature: registro-cuidados] [usability] Las personas entienden y usan apodos de sus plantas de forma consistente, y el chat los distingue sin errores. (#13)
