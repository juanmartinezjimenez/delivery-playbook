# 2. Analizar

**Objetivo:** decidir qué resolver primero.
**Entregable:** lista priorizada de oportunidades con ROI estimado.

## Estimar el valor

Para cada problema del diagnóstico:

```text
ahorro mensual = veces al mes × minutos por vez ÷ 60 × coste por hora
```

Ejemplo: 400 tareas al mes × 4 minutos ÷ 60 × 20 €/h = **533 €/mes**.

Si el problema no es de tiempo sino de ingresos (clientes que no se contestan,
presupuestos que no se siguen), estima el valor con la tasa de conversión
perdida, y dilo explícitamente: es una estimación más débil.

## Priorizar

Cada oportunidad se coloca en una matriz de valor × esfuerzo:

| | Esfuerzo bajo | Esfuerzo alto |
| --- | --- | --- |
| **Valor alto** | Hacer primero | Planificar por fases |
| **Valor bajo** | Hacer si sobra tiempo | Descartar |

El primer proyecto con un cliente debe estar en la casilla de arriba a la
izquierda: resultado visible en semanas, no en meses.

## ¿Regla, automatización o IA?

| Si el problema… | Se resuelve con |
| --- | --- |
| Siempre sigue los mismos pasos y los datos están estructurados | Regla o automatización determinista |
| Necesita leer texto libre, documentos o imágenes | Extracción con IA + validación determinista |
| Necesita conversar o decidir con contexto ambiguo | Agente de IA con límites y paso a humano |

La IA es la última opción, no la primera ([ADR 0002](adr/0002-reglas-antes-que-ia.md)).

## Salida de la fase

Una tabla con cada oportunidad, su valor estimado, su esfuerzo y el tipo de
solución. Es la base de la propuesta.
