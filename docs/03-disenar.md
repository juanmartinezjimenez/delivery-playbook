# 3. Diseñar

**Objetivo:** el sistema más pequeño que resuelve el problema priorizado.
**Entregable:** [propuesta](../templates/propuesta.md) y decisiones técnicas registradas como ADR.

## Criterios, en este orden

1. **Retorno:** el coste total (construcción + operación) se recupera en meses, no en años.
2. **Simplicidad operativa:** alguien que no lo ha construido puede operarlo con el runbook.
3. **Datos del cliente, en manos del cliente:** infraestructura y cuentas a su nombre siempre que sea posible.
4. **Bajo mantenimiento:** pocas piezas, piezas estándar.
5. **Escalable cuando haga falta:** no antes.

## Construir o comprar

| Pregunta | Si la respuesta es sí |
| --- | --- |
| ¿Existe una herramienta que lo hace y su coste es razonable? | Comprar o integrarse |
| ¿El proceso es el diferencial del negocio? | Construir |
| ¿Hay que pagar por usuario y el equipo va a crecer? | Valorar una alternativa self-hosted |

## Qué debe quedar escrito

- **Diagrama de arquitectura:** qué piezas hay y qué habla con qué.
- **Modelo de datos:** qué se guarda, dónde y durante cuánto tiempo.
- **ADR por cada decisión cara de revertir:** base de datos, proveedor de IA, dónde se aloja, qué queda fuera de alcance.
- **Qué pasa cuando falla:** cada integración tiene un comportamiento definido ante error (reintento, cola, aviso a una persona).

## Errores comunes

- Diseñar para 1.000 clientes cuando hay 3.
- Meter un LLM en un paso que es una regla.
- Dejar el "qué pasa si falla" para después: después es en producción.
