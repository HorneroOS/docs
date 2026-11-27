# Actualizar una instalación existente a preview29

> Traducción al español rioplatense de la
> [versión en inglés](../../getting-started/upgrading-to-preview29.md), que es
> la canónica.

Este anexo lleva un sistema que ya siguió
[Actualizar una instalación preview24 existente](upgrading-from-preview24.md)
(o que se instaló desde preview25–preview28) a la composición de paquetes
publicada en **v0.2.0-preview29**, sin reinstalar.

Preview29 no cambia la composición de ediciones. La diferencia está a nivel de
paquetes:

- `horneroctl-bin` `0.2.0_preview37-1`: `horneroctl gaming doctor` diagnostica
  la coherencia entre módulo NVIDIA y kernel (variantes `nvidia-open`, `-lts` y
  `-dkms`) y la informa como un chequeo único.
- `hornero-config` `0.3.15-1`: el entorno de Hyprland ya no fuerza
  `LIBVA_DRIVER_NAME=nvidia`; VA-API autoselecciona el controlador para la GPU
  que realmente está presente.

## Pasos

1. Actualizá los paquetes de Arch (actualización completa, nunca parcial):

   ```bash
   sudo pacman -Syu
   ```

2. Actualizá los paquetes de HorneroOS en el AUR. `pacman -Syu` y
   `horneroctl package upgrade` **no** actualizan paquetes del AUR; recompilalos
   con tu ayudante de AUR o manualmente, por ejemplo:

   ```bash
   git clone https://aur.archlinux.org/horneroctl-bin.git
   cd horneroctl-bin
   # horneroctl-bin verifica su binario firmado contra la clave de releases
   # de HorneroOS (huella FCFBEE43925AB5429362278AE59EAB44AA2498DC, fijada
   # en validpgpkeys). La clave viene con el paquete; importala una vez para
   # que makepkg pueda verificar. Los ayudantes de AUR (yay/paru) también la
   # pueden bajar de servidores públicos de claves. Nunca compiles sin firmas.
   gpg --import hornero-release.pub
   gpg --list-keys FCFBEE43925AB5429362278AE59EAB44AA2498DC
   makepkg -si
   cd ..
   git clone https://aur.archlinux.org/hornero-config.git
   cd hornero-config && makepkg -si
   pacman -Q horneroctl-bin hornero-config
   # se espera horneroctl-bin 0.2.0_preview37-1, hornero-config 0.3.15-1
   ```

   Si la compilación se detiene con
   `gpg: keyserver receive failed: No data` o
   `FAILED (unknown public key …)`, faltó el paso de importación anterior en un
   llavero que todavía no tiene la clave; ejecutalo y volvé a compilar. No lo
   esquives deshabilitando la verificación PGP.

3. Cerrá sesión y volvé a entrar para que la sesión tome el nuevo entorno de
   Hyprland (el cambio de VA-API tiene alcance de sesión).

4. Verificá:

   ```bash
   horneroctl version            # horneroctl-v0.2.0-preview37
   horneroctl gaming doctor      # sistemas Gaming; incluye gpu-driver-coherence
   horneroctl studio doctor      # sistemas Studio; todos los chequeos en verde
   ```

## Notas para usuarios de dotfiles (chezmoi)

La detección nativa de HorneroOS lee `ID=horneroos` desde `/etc/os-release`.
Las instalaciones migradas desde preview24 conservan `ID=arch` (mirá las
limitaciones conocidas de la guía de preview24), así que no se detectan como
nativas. Donde una plantilla de chezmoi lo soporte, previsualizá la migración
con el override explícito y revisá el diff antes de aplicar nada:

```bash
HORNERO_NATIVE=1 chezmoi diff
```

No corras un `chezmoi apply` destructivo como parte de esta actualización; los
pasos de paquetes de arriba no tocan tu configuración personal, perfiles de OBS
ni datos de usuario.

## Limitaciones conocidas

Las limitaciones de la guía de preview24 siguen vigentes: no hay reconciliación
de ediciones, no hay integración de snapshots/vuelta atrás, y este anexo no
modifica los stacks de controladores gráficos. `gpu-driver-coherence` solo
*informa* una discrepancia entre controlador y kernel; nunca instala ni quita
paquetes de controladores.
