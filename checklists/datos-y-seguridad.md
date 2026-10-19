# Checklist: datos y seguridad

Orientada al RGPD. No sustituye el asesoramiento legal: sirve para no olvidar nada
antes de tratar datos personales de un cliente.

## Roles y contratos

- [ ] Está claro quién es responsable del tratamiento (el cliente) y quién encargado (nosotros)
- [ ] Hay contrato de encargo del tratamiento firmado (art. 28 RGPD)
- [ ] Los subencargados (proveedor de IA, alojamiento, mensajería) están listados y el cliente los conoce
- [ ] Los proveedores fuera del Espacio Económico Europeo tienen garantías adecuadas para la transferencia

## Datos

- [ ] Solo se tratan los datos necesarios para la finalidad acordada
- [ ] Si hay categorías especiales (por ejemplo, salud), se ha revisado su base legal y medidas adicionales
- [ ] Hay un plazo de conservación definido y un proceso para borrar
- [ ] Se puede atender una solicitud de acceso o supresión de una persona concreta

## Seguridad técnica

- [ ] Cifrado en tránsito (HTTPS) en todas las conexiones
- [ ] Secretos en un gestor de secretos o variables de entorno, nunca en el código
- [ ] Copias de seguridad cifradas y con acceso restringido
- [ ] Registro de accesos administrativos

## Si algo sale mal

- [ ] Se sabe a quién avisar y en qué plazo ante una brecha de seguridad (72 h a la autoridad de control)
