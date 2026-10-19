# 5. Medir

**Objetivo:** comprobar si el sistema cumple lo que prometía la propuesta.
**Entregable:** informe breve a los 30, 60 y 90 días.

## Qué se mide

Las métricas se acuerdan en la propuesta, antes de construir. Si no se puede
medir, no se puede saber si funcionó.

| Tipo de sistema | Métrica principal | Métricas de control |
| --- | --- | --- |
| Automatización de tareas | Horas ahorradas al mes | Errores, casos que pasan a revisión manual |
| Extracción de documentos | % procesado sin intervención | Errores por campo, tiempo de revisión |
| Agente conversacional | % de conversaciones resueltas sin persona | Paso a humano, quejas, coste por conversación |
| Captación y seguimiento | Contactos recuperados o convertidos | Tiempo de primera respuesta |

## Cómo se mide

- El propio sistema registra lo necesario para calcular sus métricas: no se
  mide a mano.
- Se compara contra la situación de partida del diagnóstico.
- El coste de operación (IA, servidores, licencias) entra en el cálculo.

## Revisiones

| Momento | Pregunta |
| --- | --- |
| 30 días | ¿Funciona como se diseñó? ¿Qué casos falla? |
| 60 días | ¿Se acerca a las métricas acordadas? ¿Qué ajustar? |
| 90 días | ¿Ha cumplido? ¿Cuál es la siguiente oportunidad del diagnóstico? |

Lo aprendido en cada revisión vuelve a la fase 1: el siguiente proyecto sale
del mismo diagnóstico, ya validado con datos.
