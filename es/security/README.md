# Seguridad y privacidad

HorneroOS es una familia de sistemas operativos en etapa de desarrollo basada
en Arch Linux. Una ISO preview o un paquete de AUR no reemplazan revisar el
software, las fuentes de actualización y el modelo de amenazas en una máquina
que guarda datos importantes.

## Cifrado de disco (LUKS)

El cifrado completo de disco es opcional y se elige en el instalador
provisional Calamares durante el particionado. Nada viene preseleccionado.

- **Estado en v0.2.0-preview32:** Las instalaciones UEFI sin cifrar pasaron
  en máquinas virtuales desechables. Las instalaciones cifradas con LUKS no
  se volvieron a ejecutar sobre preview32 y no se heredan como aprobadas
  para ese artefacto.
- **El bloqueo de sesión no cifra el disco:** Bloquear el escritorio con
  **Super + L** solo protege una sesión ya en curso. Sin LUKS, cualquiera con
  acceso físico al disco puede leer tus archivos fuera de línea.

## Secure Boot

HorneroOS todavía no distribuye shims firmados para Secure Boot ni enrola
claves de Microsoft o personalizadas automáticamente.

- Arrancar la ISO preview requiere desactivar Secure Boot en el firmware,
  salvo que firmes y enroles tus propias claves (por ejemplo con `sbctl`,
  siguiendo la
  [guía de Secure Boot de ArchWiki](https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface/Secure_Boot)).
- No asumas que Secure Boot quedó activo después de instalar; verificalo con
  `bootctl status`.

## Postura de firewall

HorneroOS no instala ni habilita en silencio un perfil de firewall propio por
encima de los valores por defecto de Arch Linux.

- Revisá los sockets en escucha con `ss -tulpn` después de instalar.
- Si te conectás a redes no confiables, habilitá y configurá un firewall de
  host como `nftables` o `ufw` (ver la
  [guía de firewalls de ArchWiki](https://wiki.archlinux.org/title/Firewalls)).

## Firma y verificación de releases

Las ISO oficiales y los artefactos de release de HorneroOS se firman con la
clave GPG de releases de HorneroOS:

- **Huella:** `FCFBEE43925AB5429362278AE59EAB44AA2498DC`
- **Clave pública:** `packaging/keys/hornero-release.pub.asc` en
  [`HorneroOS/hornero`](https://github.com/HorneroOS/hornero)

Verificá siempre tanto la firma desacoplada `.sig` como el checksum `.sha256`
antes de escribir una ISO en un pendrive USB. Ver
[Primeros pasos](../getting-started/README.md) para los comandos exactos de
verificación.

## Límites de confianza de AUR

En Arch Linux, los paquetes fuera de los repositorios oficiales de Arch
provienen del Arch User Repository (AUR), mantenido por la comunidad.

- Leé cada `PKGBUILD` antes de compilar o actualizar con `yay` o `paru`.
- Nunca ejecutes `makepkg` como `root`.
- Los paquetes oficiales de HorneroOS (`hornero-shell`, `hornero-config`,
  `horneroctl-bin`, `hornero-greeter`) se compilan desde los repositorios
  bajo `github.com/HorneroOS`. Los paquetes AUR de terceros quedan fuera del
  límite de confianza de HorneroOS.

## Elevación de privilegios (polkit y sudo)

HorneroOS sigue los límites estándar de privilegios de Arch Linux:

- La elevación gráfica interactiva usa `polkit-gnome` (el agente de
  autenticación de polkit).
- La administración por terminal usa `sudo` con autenticación explícita del
  usuario.
- `horneroctl` separa la inspección de solo lectura de las acciones que
  modifican estado. Los comandos con efecto soportan `--dry-run` y requieren
  `--yes` (o confirmación interactiva) en lugar de elevar privilegios en
  silencio.

## Extensiones: QML sin sandbox vs companions de solo datos de PluginKit 6

Hornero Shell soporta dos modelos de extensión con límites de confianza
distintos:

- **Extensiones QML de la shell (sin sandbox):** Las extensiones QML corren
  dentro del proceso de Quickshell / Hornero Shell con todos los permisos de
  tu sesión de usuario. Tratá una extensión QML con el mismo cuidado que
  cualquier código ejecutable local: inspeccioná su fuente antes de
  instalarla.
- **Companions de solo datos de PluginKit 6:** Los companions instalados
  desde el catálogo de PluginKit son paquetes declarativos de datos
  (manifiestos, metadatos y acciones estructuradas) en lugar de código QML
  ejecutable arbitrario. No pueden ejecutar código arbitrario dentro del
  proceso de la shell por sí solos.

Ver la [plataforma PluginKit](../development/pluginkit-platform.md) y la
[guía de extensiones](../desktop/extensions.md) para los contratos exactos.

## Confinamiento de agentes de IA (bubblewrap)

Cuando HorneroOS lanza agentes locales de código o herramientas del asistente
mediante `horneroctl agent` / `horneroctl assistant`, el confinamiento se
apoya en espacios de nombres de `bubblewrap` (`bwrap`) donde esté soportado:

- El acceso al sistema de archivos se acota al espacio de trabajo declarado y
  a montajes de sistema de solo lectura explícitos, en lugar de todo tu
  directorio personal.
- La exposición de red y secretos debe tratarse como opt-in explícito; nunca
  asumas que el sandbox de un agente protege contra una vulnerabilidad del
  kernel o montajes demasiado amplios.
- Inspeccioná las políticas y el estado con `horneroctl assistant policy` y
  `horneroctl agent status`.

## Ubicación y clima

Sin una ubicación configurada, el clima no hace ninguna solicitud de
ubicación ni infiere tu posición desde tu IP. Ingresar una ciudad envía ese
nombre al servicio de geocodificación de Open-Meteo y después pide el
pronóstico para sus coordenadas. Ingresar coordenadas pide el pronóstico y
usa la geocodificación inversa de Nominatim para etiquetar la ubicación.
Estas solicitudes usan HTTPS. El comportamiento actual del proveedor está
implementado en
[Weather.qml](https://github.com/HorneroOS/shell/blob/main/services/Weather.qml);
revisalo de nuevo antes de activar cualquier futura función de detección de
ubicación.

## Bloqueá tu sesión

Usá **Super + L** o el menú de sesión para bloquear la sesión actual. La
pantalla de bloqueo protege el acceso a una sesión ya en curso; no cifra un
disco, no reemplaza la seguridad de la cuenta ni protege una máquina cuya
sesión quedó desbloqueada.

## Temas y archivos

Los packs de temas de Hornero describen apariencia. Una tarjeta de tema no
autoriza un paquete o script sin revisar. Hornero no descarga en silencio
assets arbitrarios de fondos o íconos. Usá fuentes de paquetes confiables y
revisá los cambios de configuración personalizados antes de aplicarlos.

## Compartir diagnósticos

Antes de publicar logs o capturas, sacá nombres de usuario, hostnames,
números de serie, nombres de redes, rutas a archivos privados, contenido de
notificaciones y salida de terminal no relacionada. Compartí solo las líneas
necesarias para reproducir el problema.

## Divulgación de vulnerabilidades

No reportes vulnerabilidades de seguridad en issues públicos de GitHub. Seguí
el proceso privado de reporte en
[`SECURITY.md`](https://github.com/HorneroOS/.github/blob/main/SECURITY.md)
(o usá GitHub Private Vulnerability Reporting en el repositorio afectado bajo
`HorneroOS`).

Para las recetas de herramientas de seguridad específicas de una máquina de
la antigua wiki de dotfiles, ver la
[disposición de la documentación](../development/dotfiles-wiki-disposition.md).
