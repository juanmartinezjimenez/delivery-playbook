# Checklist: puesta en producción

Ningún sistema se activa con usuarios reales sin pasar esta lista.

## Funcionamiento

- [ ] El piloto ha cumplido los criterios acordados en la propuesta
- [ ] Cada integración tiene un comportamiento definido ante error (reintento, cola o aviso)
- [ ] Los casos que el sistema no resuelve llegan a una persona, y esa persona lo sabe

## Entornos y datos

- [ ] Producción y pruebas no comparten base de datos ni credenciales
- [ ] No quedan datos de prueba en producción
- [ ] Hay copia de seguridad automática y se ha probado a restaurarla

## Seguridad

- [ ] Ningún secreto en el repositorio (gitleaks en CI)
- [ ] Cada servicio usa una cuenta con los permisos mínimos que necesita
- [ ] Accesos de administrador revisados y documentados

## Operación

- [ ] Hay alertas para los fallos que importan, y llegan a alguien
- [ ] Los registros permiten reconstruir qué pasó con un caso concreto
- [ ] El documento de traspaso está completo y alguien lo ha leído
- [ ] Existe un plan para volver atrás si algo sale mal

## Legal

- [ ] La [checklist de datos y seguridad](datos-y-seguridad.md) está completada
