# Portapapeles

El portapapeles de Wayland tiene dos partes: el elemento copiado actualmente,
provisto por las herramientas de portapapeles de Wayland, y un gestor opcional
de historial. La configuración de sesión de Hornero registra selecciones de
texto e imagen del portapapeles con `cliphist` cuando están instaladas las
herramientas necesarias.

## Abrir el historial del portapapeles

Presioná **Super + V** o corré:

```sh
horneroctl capture clipboard
```

La CLI elige un backend disponible. En Wayland prefiere CopyQ, después
`cliphist` y por último una lectura mínima del portapapeles actual. CopyQ abre
su interfaz gráfica. El camino CLI de `cliphist` lista entradas recientes; no
es un selector interactivo. El respaldo mínimo muestra una vista previa corta
de texto y no guarda historial.

## Qué configura Hornero

CopyQ es una dependencia opcional de `hornero-config`, que provee su
configuración base bajo `~/.config/copyq/`. Aplicar un tema puede escribir una
paleta acorde para CopyQ. `cliphist` y `wl-clipboard` son paquetes separados
del host; la sesión personal de dotfiles inicia la recolección de historial de
texto e imágenes con `wl-paste --watch`.

El contenido del portapapeles puede incluir contraseñas, tokens o texto
privado. Tratá el historial como datos sensibles. Revisá los ajustes de
retención y privacidad de CopyQ y limpiá los elementos que no quieras guardar.
Hornero no promete historial de portapapeles cifrado ni sincronización entre
dispositivos.

Solución de problemas:

- Si el historial está vacío, verificá si hay un backend de historial
  instalado y si el recolector de sesión está corriendo.
- Si CopyQ no abre, corré `horneroctl capture clipboard --backend copyq` y
  verificá que CopyQ arranque por sí solo.
- Si los colores de CopyQ quedaron viejos, volvé a aplicar el tema activo
  desde Ajustes → Apariencia.

Upstream: [manual de CopyQ](https://copyq.readthedocs.io/en/latest/),
[cliphist](https://github.com/sentriz/cliphist),
[wl-clipboard](https://github.com/bugaevc/wl-clipboard).
