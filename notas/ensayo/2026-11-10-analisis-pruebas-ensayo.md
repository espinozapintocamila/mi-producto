---
source: synthetic
tests: product/tests/2026-11-10-1928-olvido-riego.md
results:
  - notas/ensayo/2026-11-10-hoja-captura-t1-ficticia.md
  - notas/ensayo/2026-11-10-hoja-captura-t2-ficticia.md
nota: ENSAYO con respuestas ficticias generadas con IA. No es evidencia sobre el segmento, no decide nada sobre las alternativas y no anota ninguna creencia.
date: 2026-11-10
---

# Análisis de pruebas (ENSAYO): olvido-riego

## Procedencia

Las 6 "personas" (E-1 a E-6) son respuestas ficticias: `synthetic`. El ensayo sirve para practicar el análisis y para encontrar fallas en el diseño antes de la prueba real, que sigue pendiente.

## T1. registro-cuidados (umbral: al menos 2 de 3 consultan la fecha 2 veces o más y esperan al menos una vez)

| Persona | Consultas | Esperó por la fecha | ¿Cuenta? |
|---|---|---|---|
| E-1 | 3 (1 sin registro) | 1 (monstera: "hacía 4 días") | sí |
| E-2 | 1 | 0 ("yo miro la tierra igual") | no |
| E-3 | 3 (1 sin registro) | 2 (una porque la pareja había regado) | sí |

- **Resultado (ensayo):** `passed`, 2 de 3. Con datos reales, la regla diría `continue`.
- **Lo que mostró el ensayo:**
  - Las consultas "sin registro" (la persona no había avisado el riego) no pueden ayudar a decidir, y con la regla original sumaban igual. Con la regla nueva, E-1 y E-3 tendrían 2 consultas con registro y seguirían contando.
  - Una de las esperas de E-3 fue porque otra persona de la casa había regado: eso es `coordinacion-riego`, no memoria propia.

## T2. guia-riego (umbral: al menos 2 de 3 hacen un cambio concreto en una planta)

| Persona | Cambios concretos | ¿Preguntó? | ¿Cuenta? |
|---|---|---|---|
| E-4 | 2 (sacó la calathea de la ventana; esperó a que se secara la monstera) | sí | sí |
| E-5 | 0 ("¡muy útil!", pero no cambió nada) | sí (invierno, tierra) | no |
| E-6 | 0 (solo una intención: "lo voy a mover") | no | no |

- **Resultado (ensayo):** `failed`, 1 de 3.
- **Lo que mostró el ensayo:** la regla de decisión no cubría el caso "1 cuenta y hubo preguntas": change exigía que nadie contara y discard exigía que no hubiera preguntas. Además, la intención de E-6 no se pudo verificar porque la prueba terminaba el día 7.

## Arreglos aplicados al diseño antes de la prueba real

1. **T2, regla de decisión completada:** change si cuentan 1 o ninguna y hubo preguntas; discard si cuentan 1 o ninguna y nadie preguntó.
2. **T1, consultas sin registro:** se anotan aparte y no suman al umbral.
3. **T1, hogares compartidos:** las esperas porque otra persona de la casa regó se anotan aparte; cuentan, pero se informan separadas.
4. **T2, intenciones:** mensaje el día 10 solo para quien declaró una intención; si lo hizo, cuenta.

Pendiente, no aplicado: las preguntas de E-5 sobre invierno y tierra sugieren que la tarjeta podría necesitar la estación del año. Quedó como parte de la versión "change" de T2.

## Decisión

Ninguna. Un ensayo no decide sobre las alternativas: A1 y A2 siguen en prueba, y T1 y T2 siguen `ready` para la prueba real con R-13, R-31 y R-36 (T1) y R-25, R-32 y R-33 (T2).
