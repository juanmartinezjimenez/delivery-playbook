# Checklist: agente de IA

Para cualquier sistema donde un modelo de lenguaje hable con clientes, extraiga
datos o tome decisiones.

## Calidad medida

- [ ] Existe un conjunto de casos de prueba con la respuesta esperada (incluidos casos difíciles y fuera de tema)
- [ ] Hay una métrica de calidad y un umbral mínimo para pasar a producción
- [ ] Los casos de prueba se ejecutan antes de cada cambio de prompt o de modelo

## Límites

- [ ] El agente sabe qué no puede hacer y lo dice en lugar de inventar
- [ ] Las acciones con efecto real (reservar, cobrar, enviar) se confirman o pasan por reglas
- [ ] Hay un paso a persona claro, y el usuario sabe cuándo habla con una máquina
- [ ] La salida estructurada se valida con reglas (formatos, totales, rangos)

## Coste y rendimiento

- [ ] Coste por conversación o por documento estimado y con límite de gasto
- [ ] Tiempo de respuesta aceptable para el canal
- [ ] Comportamiento definido si el proveedor de IA no responde

## Trazabilidad

- [ ] Cada interacción queda registrada con la versión del prompt y del modelo
- [ ] Se pueden revisar las respuestas marcadas como incorrectas
- [ ] Los datos personales enviados al modelo son los mínimos necesarios
