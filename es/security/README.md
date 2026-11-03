# Seguridad y privacidad

Hornero todavía es un proyecto de escritorio en etapa de desarrollo. Un
paquete de Arch o una release preview no reemplazan el revisar el
software y la fuente de actualizaciones en una máquina que guarda datos
importantes.

## Ubicación y clima

Sin una ubicación configurada, el clima no hace ninguna solicitud de
ubicación ni infiere tu posición desde tu IP. Ingresar una ciudad envía
ese nombre al servicio de geocodificación de Open-Meteo y después pide
el pronóstico para sus coordenadas. Ingresar coordenadas pide el
pronóstico y usa la geocodificación inversa de Nominatim para etiquetar
la ubicación. Estas solicitudes usan HTTPS. El comportamiento actual del
proveedor está implementado en
[Weather.qml](https://github.com/HorneroOS/shell/blob/main/services/Weather.qml);
revisalo de nuevo antes de activar cualquier futura función de detección
de ubicación.

## Bloqueá tu sesión

Usá **Super + L** o el menú de sesión para bloquear la sesión actual. La
pantalla de bloqueo protege el acceso a una sesión ya en curso; no cifra
un disco, no reemplaza la seguridad de la cuenta ni protege una máquina
cuya sesión quedó desbloqueada.

## Temas y archivos

Los packs de temas de Hornero describen apariencia. Una tarjeta de tema
no autoriza un paquete o script sin revisar. Hornero no descarga en
silencio assets arbitrarios de fondos o íconos. Usá fuentes de paquetes
confiables y revisá los cambios de configuración personalizados antes de
aplicarlos.

## Compartir diagnósticos

Antes de publicar logs o capturas, sacá nombres de usuario, hostnames,
números de serie, nombres de redes, rutas a archivos privados, contenido
de notificaciones y salida de terminal no relacionada. Compartí solo las
líneas necesarias para reproducir el problema.

Para las recetas de herramientas de seguridad específicas de una máquina
de la antigua wiki de dotfiles, ver la
[disposición de la documentación](../../development/dotfiles-wiki-disposition.md).
