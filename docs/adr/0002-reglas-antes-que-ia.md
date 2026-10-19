# 0002. Reglas antes que IA

- Estado: aceptada
- Fecha: 2026-10-19

## Contexto

Los modelos de lenguaje permiten resolver casi cualquier paso de un proceso,
pero cada paso resuelto con IA añade coste por ejecución, latencia, resultados
no deterministas y la necesidad de evaluar su calidad de forma continua.

## Decisión

Un paso se resuelve con IA solo si una regla determinista no puede resolverlo
con calidad suficiente. Cuando se usa IA:

- su salida se valida con reglas siempre que sea posible (formatos, totales, rangos);
- el modelo puede bajar la confianza de un resultado, nunca subirla;
- existe un camino a revisión humana para los casos dudosos;
- su calidad se mide con un conjunto de casos de prueba antes y después de cada cambio.

## Alternativas consideradas

| Opción | Por qué no |
| --- | --- |
| IA en todos los pasos | Más coste, más difícil de depurar, errores silenciosos |
| No usar IA | Deja fuera los problemas con texto libre, documentos e imágenes, donde aporta más valor |

## Consecuencias

Los sistemas son más baratos de operar y más fáciles de depurar. La IA se
concentra donde aporta valor real, y cada uso de IA tiene su validación y su
medición.
