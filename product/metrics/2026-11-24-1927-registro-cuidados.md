---
spec: product/specs/2026-11-17-2300-registro-cuidados.md
exposure-plan: product/exposure-plans/2026-11-17-2308-registro-cuidados.md
level: 1 — Registrar riegos por mensaje
status: designed
---

# Métricas de: Registro de cuidados por mensaje

## Audiencia objetivo

6 personas con más de 15 plantas de interior que aceptaron conversar en la encuesta y no trabajan con plantas (segmento del overview + audiencia del nivel 1). Cuenta cada persona, no el hogar. n=6: cada persona pesa 17 puntos; toda lectura es direccional.

## Frecuencia esperada

Al menos un riego por semana — `assumption`. La encuesta no preguntó cada cuánto riegan; solo lo sugiere la persona carolina-vidal (synthetic). Ventana de retención: semanal (días 1–7 y 8–14 de cada persona, desde que arma su lista).

## Acquisition

- **Señal:** la persona manda al chat la lista de sus plantas.
- **Definición ampliada:** lista con más de 15 plantas, dentro de los 3 días siguientes a la invitación.
- **Cálculo:** personas que armaron su lista / 6.
- **Meta:** 100% (6 de 6) · **Por qué:** se invita a cada persona directamente; si alguien no arma su lista, la entrada tiene fricción.
- **Eventos:** `invitacion_enviada`, `lista_creada` (persona, cantidad_plantas, fecha_hora).

## Activation

- **Señal:** la persona registra riegos por mensaje.
- **Definición ampliada:** riegos de 3 o más plantas distintas de su lista en sus primeros 7 días; pueden ir en un solo mensaje.
- **Umbral de la señal:** 3 plantas distintas · **Por qué:** con más de 15 plantas, la duda aparece entre varias; un registro de una sola planta no sirve para la consulta del nivel 2 (#10). El número 3 es un juicio, sin datos que lo midan. · **Excluye:** solo armar la lista, o probar con una planta.
- **Cálculo:** personas con 3+ plantas registradas en 7 días / 6.
- **Meta:** 83% (5 de 6) · **Por qué:** debe ser mayor que la de retención para que el embudo tenga sentido.
- **Límite:** en el nivel 1 la consulta está oculta; esto mide que deje un registro útil, no que riegue mejor (#10).
- **Eventos:** `riego_registrado` (persona, planta, fecha_riego, fecha_hora_mensaje, nivel).

## Retention

- **Señal:** la persona registra al menos un riego por semana.
- **Definición ampliada:** al menos un riego en la semana 1 y otro en la semana 2, sin recordatorios. Cuenta la fecha en que se regó.
- **Curva de retención:** una cohorte, quienes armaron su lista; % con 1+ riego en la semana 1 y en la semana 2. Con dos puntos no se puede ver si la curva se aplana.
- **Cálculo:** personas con 1+ riego en ambas semanas / 6. Se informa aparte cuántas de ellas activaron.
- **Meta:** 67% (4 de 6) · **Por qué:** es el criterio para avanzar del nivel 1 (#11; 2 semanas no prueban las 4 que dice la creencia).
- **Eventos:** `riego_registrado`.

## Satisfaction

- **Instrumento:** CSAT de 1 a 5 por el chat · **Pregunta:** "Del 1 al 5, ¿qué tan conforme quedaste con registrar tus riegos por este chat?" · **Cuándo:** día 14, a las 6 personas, incluidas las que dejaron de usarlo · **Corte:** 4 o más.
- **Definición ampliada:** quien no responde no cuenta como satisfecha.
- **Cálculo:** personas con 4 o 5 / 6. La tasa de respuesta y el % entre quienes responden van aparte.
- **Meta:** 67% (4 de 6) · **Por qué:** mismo piso que retención, para ver si quienes vuelven también están conformes.
- **Eventos:** `csat_enviado`, `csat_respondido` (persona, nota, fecha_hora).

## Métricas de negocio

Del overview, como están declaradas: precio de ~$1.990 CLP al mes (#3) y permanencia a los 3 meses (#4). Ninguna se lee en el nivel 1.

## Reconciliación con el plan de exposición

- **Avanzar si** 4 de 6 registran en cada una de las 2 semanas → retention ≥ 67%.
- **Detener si** 2 o menos lo hacen → retention ≤ 33%.
- **3 de 6** (hueco del plan, decidido por Cami el 2026-11-24): se repite el nivel 1, 2 semanas, con otras 6 personas del segmento. Se lee por separado, sin sumar los grupos: avanza con 4 o más y se detiene con 3 o menos.
- **Apodos (#13)**, más de 1 de cada 5 mensajes sin entender → no lo lee ninguna métrica AARS; requiere el evento `mensaje_no_entendido` (persona, texto, fecha_hora).
