# Empaquetado y entrega

HorneroOS se ensambla a partir de varios repositorios y paquetes. Esta página
es para colaboradores que cambian cómo llega el código fuente a un sistema
instalado; no es una guía de instalación para usuarios finales. La ISO
firmada `v0.2.0-preview42` y la QCOW2 preinstalada de Desktop se entregan
fuera de banda (Vercel Blob, con checksum, firma y manifiesto en el release
de GitHub); esta página cubre la entrega de paquetes. Mirá
[Primeros pasos](../getting-started/README.md) para el estado actual.

## Límites de entrega

| Origen | Responsabilidad entregada |
| --- | --- |
| [`config`](https://github.com/HorneroOS/config) | Valores por defecto, paquetes de temas, assets y materialización de configuración del sistema. |
| [`shell`](https://github.com/HorneroOS/shell) | Runtime Quickshell y sus servicios/módulos. |
| [`hornero`](https://github.com/HorneroOS/hornero) | `horneroctl` y operaciones soportadas orientadas al SO. |
| [`greeter`](https://github.com/HorneroOS/greeter) | Paquete del tema SDDM greeter de Hornero. |
| [`website`](https://github.com/HorneroOS/website) | Información pública del producto y pines revisados a datos fuente y docs. |

Los releases de repositorios, las recetas de paquetes y los pines entre
repositorios forman el contrato de entrega. Revisá la página de releases actual
antes de presentar cualquier paquete como disponible de forma general. No
infieras un camino de instalación soportado por el hecho de que un componente
individual pueda empaquetarse.

## Datos de usuario y valores de fábrica

Tratá el contenido de `/usr/share` como propiedad del paquete y de solo
lectura. Los cambios del usuario pertenecen a las ubicaciones documentadas de
configuración y datos del usuario. Las actualizaciones de paquetes no deben
sobrescribir silenciosamente archivos propiedad del usuario. Validá los valores
por defecto modificados en un entorno limpio fiel al paquete, preservá los
overrides explícitos del usuario y evitá arrastrar rutas o formatos obsoletos
sin un contrato soportado de actualización en sitio. Nunca copies archivos
específicos de la máquina de un desarrollador a los valores por defecto del
paquete.

## Validación de releases

Antes de un release o una actualización de pines, verificá las revisiones
fuente exactas, el contenido de los paquetes, las declaraciones de dependencias
y un entorno limpio fiel al paquete. Para cambios que cruzan repositorios,
actualizá los pines recién después de que el cambio de origen esté revisado y
mergeado. Usá el proyecto Hornero QA existente para aceptación gráfica cuando
corresponda; no sustituyas dependencias empaquetadas del producto por los
dotfiles de un desarrollador.

El flujo detallado de empaquetado y releases pertenece a la documentación de
colaboradores de cada repositorio implementador. Este manual registra los
límites y enlaces en vez de duplicar esos procedimientos.
