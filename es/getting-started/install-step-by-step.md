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
- Tanto UEFI como Legacy BIOS están validados en KVM sobre la ISO
  `v0.2.0-preview42`, junto con el uso diario en producción sobre
  estaciones físicas. Preferí UEFI en hardware moderno cuando esté
  disponible. Mirá
  [Hardware: probado y no probado](../hardware/tested-and-untested.md).
- El cifrado completo con LUKS y copy-to-RAM están disponibles en el
  instalador; probá siempre tu equipo en modo Live primero si tenés
  hardware particular.

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
3. Compositor: Hyprland es el compositor por defecto; Niri también está
   soportado como opción de compositor Wayland con columnas desplazables
   (mirá [Compositores Wayland](../desktop/compositors.md) para ver las
   diferencias de capacidades).
4. Disco: preferí todo el disco o un esquema manual que entiendas
   antes que una opción alongside/resize sin respaldo. El cifrado
   completo con LUKS es opcional y se elige durante el particionado.
5. Usuario: creá tu cuenta de todos los días con una contraseña
   fuerte. Con esa cuenta vas a actualizar y configurar.

La ISO usa el instalador gráfico Calamares (`3.4.3`). Si falla, reiniciá
antes de reintentar y reportá el fallo en el
[selector de issues del instalador](https://github.com/HorneroOS/installer/issues/new/choose)
con nombre de ISO, firmware, elección de cifrado y paso exacto.

## Primer arranque

Retirá el pendrive y arrancá el sistema instalado. Después seguí
[Primeros pasos después de instalar](../applications/post-install-first-steps.md).
Si la máquina no arranca, mirá
[Solución de problemas por síntoma](../troubleshooting/by-symptom.md).
