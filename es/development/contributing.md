# Contribuir

> Traducción al español rioplatense de la
> [versión en inglés](../../development/contributing.md), que es la canónica.

Los cambios de HorneroOS se revisan en el repositorio que es dueño de ellos.
Antes de empezar, revisá los pull requests y los issues abiertos para no
duplicar trabajo en paralelo, y leé las instrucciones de contribución de ese
repositorio.

## Una contribución enfocada

1. Enunciá el problema para la persona usuaria y el comportamiento esperado.
2. Identificá el repositorio dueño y cualquier consumidor aguas abajo.
3. Creá una rama enfocada desde el `main` actual del repositorio canónico.
4. Seguí las instrucciones de estilo y de pruebas del repositorio.
5. Para trabajo visual, incluí evidencia de ejecución antes/después y ejercitá
   la interacción modificada.
6. Actualizá la documentación de usuario y los datos del producto cuando cambie
   su verdad.
7. Pedí revisión y resolvé los comentarios antes de fusionar.

Para trabajo entre repositorios, aterrizá primero el cambio en la fuente de
verdad y después actualizá a los consumidores hacia revisiones revisadas.
Preservá la autoría de quien contribuyó al mover trabajo existente. No hagas
force-push sobre trabajo que no es tuyo ni saltees las protecciones de rama del
repositorio.

Usá [Pruebas](testing.md) para elegir la evidencia de aceptación y
[Arquitectura](../architecture/README.md) para identificar a quién pertenece
cada cambio.
