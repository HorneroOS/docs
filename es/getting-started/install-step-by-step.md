# Instalar HorneroOS paso a paso

HorneroOS es un sistema operativo para uso diario: se usa y se
mantiene todos los días, con limitaciones concretas y declaradas.
Esta guía instala la ISO publicada en una máquina real o virtual.
El archivo ISO conserva su nombre publicado; ese nombre es de
artefacto, no una indicación de cómo podés usar el sistema a diario.

## Antes de empezar

- Respaldá todo lo que quieras conservar del disco destino.
  Confirmar una operación de particionado en el instalador puede
  borrar datos.
- Preferí firmware UEFI. Legacy BIOS, instalaciones cifradas con
  LUKS, sesiones Niri y copy-to-RAM no se corrieron en la ISO
  v0.2.0-preview32 y hoy son limitaciones concretas, no pasos que
  esta guía pueda prometer. Mirá
  [Hardware: probado y no probado](../hardware/tested-and-untested.md).
- El alcance validado de esa ISO es instalaciones Desktop, Studio
  y Gaming UEFI sin cifrar en máquinas virtuales descartables.
  Ese artefacto todavía no tiene validación en hardware físico.

## Descargar y verificar

Seguí [Primeros pasos](README.md) para descargar y verificar
SHA-256 y GPG. No te saltees la verificación: escribí solo una
imagen cuyo checksum y firma pasen los dos.

## Escribir el pendrive y arrancar

Usá un escritor gráfico en el que confíes, o `dd` como muestra
[Primeros pasos](README.md). Confirmá antes el dispositivo de
disco completo con `lsblk`; escribir en el dispositivo equivocado
destruye sus datos.

Arrancá desde el pendrive, desactivá Secure Boot si tu firmware
bloquea el sistema live y confirmá que el instalador ve tu disco.
Si falta un NVMe interno en una laptop Intel, mirá la nota VMD/RST
en [Solución de problemas](../troubleshooting/README.md).

## Qué elegir hoy en el instalador

1. Idioma, teclado y zona horaria: elegí tu configuración real;
   el teclado lo podés cambiar después desde el escritorio.
2. Edición: Desktop para uso general, Studio para audio y trabajo
   creativo, Gaming para jugar. Las tres salen de la misma ISO.
3. Compositor: Hyprland es el validado por defecto. Elegí Niri
   solo si aceptás una sesión experimental con superficie
   verificada menor.
4. Disco: preferí todo el disco o un esquema manual que entiendas
   antes que una opción alongside/resize sin respaldo. El
   instalador ofrece LUKS, pero las instalaciones cifradas no se
   validaron en esta ISO; elegilo conociendo ese límite.
5. Usuario: creá tu cuenta de todos los días con una contraseña
   fuerte. Con esa cuenta vas a actualizar y configurar.

El instalador es el Calamares provisorio. Si falla, reiniciá antes
de reintentar y reportá el fallo en el
[selector de issues del instalador](https://github.com/HorneroOS/installer/issues/new/choose)
con nombre de ISO, firmware, elección de cifrado y paso exacto.

## Primer arranque

Retirá el pendrive y arrancá el sistema instalado. Después seguí
[Primeros pasos después de instalar](../applications/post-install-first-steps.md).
Si la máquina no arranca, mirá
[Solución de problemas por síntoma](../troubleshooting/by-symptom.md).
