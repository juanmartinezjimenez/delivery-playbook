# 4. Implementar

**Objetivo:** poner el sistema en producción sin sorpresas.
**Entregable:** sistema funcionando y [documento de traspaso](../templates/traspaso.md).

## Flujo de trabajo

1. **Repositorio desde plantilla**, con CI y control de secretos desde el primer commit.
2. **Entornos separados:** pruebas y producción nunca comparten base de datos ni credenciales.
3. **Datos de prueba sintéticos.** Los datos reales solo existen en producción.
4. **Cambios pequeños**, en ramas, revisados antes de llegar a `main`.
5. **Piloto con volumen real reducido** antes de activar todo: por ejemplo, una semana o 50 casos.

## Durante el piloto

- Revisar cada caso que el sistema no resuelve solo y apuntar por qué.
- Ajustar reglas y prompts con esos casos, no con suposiciones.
- No ampliar alcance hasta que el piloto cumpla los criterios acordados en la propuesta.

## Antes de activar

Pasar la [checklist de puesta en producción](../checklists/puesta-en-produccion.md)
y, si hay IA de por medio, la [checklist de agente de IA](../checklists/agente-ia.md).

## Traspaso

El sistema no está entregado hasta que existe un runbook que permite a otra
persona operarlo: qué hace, cómo se comprueba que funciona, qué alertas hay y
qué hacer ante cada fallo conocido.
