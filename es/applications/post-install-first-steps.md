# Primeros pasos después de instalar

Tu primera media hora en una instalación nueva de HorneroOS, en
orden. Nada de esto requiere reiniciar hasta que una actualización
lo pida.

## 1. Revisá el sistema tal como quedó instalado

```sh
horneroctl doctor
```

Corregí o anotá lo que reporte antes de cambiar configuración.
El doctor es de solo lectura: reporta sesión Wayland, terminal,
rutas de configuración y temas que encuentra.

![Una terminal con la salida de doctor: catorce chequeos con marcas
OK, sesión Wayland, terminal elegida, rutas de configuración del
shell y temas Qt, terminando con "all 14 checks
passed".](https://www.horneroos.com/captures/cap-term-04.png)

*Salida de ejemplo de `doctor` en la máquina del mantenedor — las
rutas son su home; las tuyas van a diferir. Captura,
19 de noviembre de 2026.*

## 2. Buscá actualizaciones antes de instalar nada

```sh
horneroctl package check
horneroctl package upgrade --dry-run
```

Leé la lista pendiente. Actualizar es una actualización completa
de sistema Arch y no crea snapshot de sistema; mirá
[Actualizaciones y recuperación](../desktop/updates-and-rollback.md)
antes de confirmar con `--yes`.

## 3. Guardá tu configuración inicial

```sh
horneroctl config snapshot create --dry-run
horneroctl config snapshot create --yes
horneroctl config snapshot list
```

Un snapshot de configuración guarda solo ajustes de Hornero. No
es un snapshot de sistema y no puede deshacer una actualización
de paquetes.

![Página Updates & backups de Settings. El área de actualizaciones
todavía está chequeando, backups dice "No backups yet", y abajo
están restore de snapshot de configuración y
dependencias.](https://www.horneroos.com/captures/cap-cc-10.png)

*Settings → Updates en una máquina sin backups. Nada en esta
página es rollback de sistema. Captura de escritorio en ejecución
de la máquina del mantenedor, 19 de noviembre de 2026.*

## 4. Elegí el modo para el trabajo que tenés enfrente

```sh
horneroctl mode list
horneroctl mode set everyday
horneroctl mode status
```

Usá `horneroctl mode set studio` o `horneroctl mode set gaming`
cuando ese sea el trabajo que vas a hacer. Los modos se describen
en [Modos de experiencia](../desktop/experience-modes.md).

## 5. Recorré el Centro de control una vez

Abrí Settings y revisá Network, Displays, Sound y Updates en ese
orden. Confirmá que la disposición de pantallas coincide con tus
monitores antes de tocar apariencia.

![Página Layout de Settings con una grilla de presets de barras
con miniaturas de topología. Cockpit, top plus bottom, está
marcado como layout activo.](https://www.horneroos.com/captures/cap-cc-02.png)

*Settings → Layout: elegís una disposición y se aplica al toque.
Captura de la máquina del mantenedor, 19 de noviembre de 2026,
reutilizada de [Layouts](../desktop/layouts.md).*

## 6. Instalá aplicaciones desde el catálogo

Instalá aplicaciones opcionales con el flujo de paquetes que tu
instalación ya usa, y revisá antes el estado en el
[catálogo de aplicaciones](../../applications/catalogue.md): separa instalado,
opt-in y planificado, así un launcher planificado nunca se
presenta como instalado.

## Si algo ya anda mal

Andá a [Solución de problemas por síntoma](../troubleshooting/by-symptom.md)
y empezá por el síntoma, no por una solución que encontraste en
otro lado.
