# Probar cambios de HorneroOS

> Traducción al español rioplatense de la
> [versión en inglés](../../development/testing.md), que es la canónica.

Elegí evidencia acorde al riesgo. Una edición pura de documentación necesita
chequeos de enlaces y markdown; un cambio de interacción en la Shell necesita
entrada real y evidencia renderizada; un cambio de paquete o tema necesita
comprobarse fuera del entorno de dotfiles de la persona dueña.

## Antes de probar

1. Leé las instrucciones de prueba del repositorio destino e inspeccioná los
   cambios exactos que estás probando.
2. Mantené los datos de prueba bajo un directorio temporal o una VM descartable.
   Nunca archives el directorio home de un desarrollador ni apliques
   configuración de prueba sobre un host en uso.
3. Deshabilitá la telemetría o los reportes donde el entorno de prueba lo
   soporte.
4. Mantené la concurrencia de VM y compilación dentro de los límites de memoria
   y CPU disponibles.

## Aceptación gráfica

Usá el [repositorio Hornero QA](https://github.com/HorneroOS/qa) existente
cuando un escenario establecido cubra el comportamiento. Conducí los recorridos
de usuario con entrada de teclado y puntero, y usá capturas o grabaciones para
inspeccionar la salida real. Los chequeos determinísticos establecen la
aceptación; la revisión visual explica si la experiencia es coherente. No trates
una llamada a comando o API como prueba de una interacción de usuario salvo que
la API misma esté bajo prueba.

Para trabajo de apariencia, verificá que el tema seleccionado, el modo, la
paleta de la Shell, GTK, los íconos y el fondo de pantalla informen el estado
esperado. Para trabajo de Ajustes, verificá la navegación con mouse y teclado,
el foco visible, la persistencia y la recuperación ante dependencias no
disponibles. Las afirmaciones válidas solo para paquetes requieren un entorno
fiel al empaquetado, sin dotfiles personales que suplan archivos faltantes.

## Evidencia e informes

Conservá la evidencia útil junto con la corrida de prueba y preservá su
procedencia. Las imágenes públicas del producto deben curarse deliberadamente a
partir de capturas genuinas en tiempo de ejecución; las capturas de depuración y
los contenidos privados de escritorio no son material público. Registrá la
revisión probada y el entorno cuando esos datos afecten la interpretación.

Seguí los comandos de CI y prueba de cada repositorio. No introduzcas un
framework de pruebas nuevo cuando un chequeo existente ya pueda probar el
comportamiento requerido.
