# Aplicaciones de Gaming

Matriz verificada de aplicaciones, origen, licencia y soporte para HorneroOS
Gaming. Esta página es una vista de lectura del catálogo canónico de Hornero
([`editions/catalogue.yaml`](https://github.com/HorneroOS/hornero/blob/main/editions/catalogue.yaml)
en HorneroOS/hornero); no es un segundo catálogo. Si esta página y el catálogo
difieren, gana el catálogo y esta página está desactualizada.

**Última verificación: 2026-11-03** contra el
[índice de paquetes de Arch](https://archlinux.org/packages/). La presencia de
un paquete no equivale a soporte de Hornero: Gaming es una edición
**Soportada** (HorneroOS/hornero#328) que se instala desde la ISO compartida
firmada (validada en hardware físico y KVM); ningún juego ni lanzador de
terceros de abajo está certificado por Hornero en cualquier hardware.

## Perfiles

Las selecciones de Gaming son perfiles componibles (especializaciones), no un
paquete fijo:

| Perfil | Significado | Estado |
| --- | --- | --- |
| Desktop Gaming | Perfil por defecto de gaming | Soportado |
| Handheld | Sesión centrada en control | Planificado — sin calificar |
| Streaming | Captura y grabación con OBS Studio | Soportado |
| Multi-Launcher | Lutris, Bottles y runners de Wine | Planificado |
| VR | Camino SteamVR | Experimental — solo referencia |
| Advanced Compatibility | Opt-ins del usuario para Proton/Wine | Planificado |

## Matriz

| Aplicación | Paquetes | Origen | Licencia | Instalación | Estado | Perfiles |
| --- | --- | --- | --- | --- | --- | --- |
| Steam | steam | [arch-multilib](https://archlinux.org/packages/multilib/x86_64/steam/) | propietaria (Steam Subscriber Agreement) | pacman-repository-opt-in | Soportado — solo opt-in | Desktop Gaming, Handheld, VR |
| Lutris | lutris | [arch-extra](https://archlinux.org/packages/extra/x86_64/lutris/) | open-source (GPL-3.0-or-later) | pacman-repository | Planificado | Multi-Launcher |
| Bottles | bottles | [AUR](https://aur.archlinux.org/packages/bottles) (manual) | open-source (GPL-3.0-or-later) | manual | Planificado — solo manual | Multi-Launcher |
| Wine | wine | [arch-multilib](https://archlinux.org/packages/multilib/x86_64/wine/) | open-source (LGPL-2.1-or-later) | pacman-repository | Planificado | Multi-Launcher, Advanced Compatibility |
| vkBasalt | vkbasalt (+ lib32 vía AUR) | [arch-extra](https://archlinux.org/packages/extra/x86_64/vkbasalt/) | open-source (MIT) | pacman-repository / manual | Planificado | Advanced Compatibility |
| OBS Studio | obs-studio | [arch-extra](https://archlinux.org/packages/extra/x86_64/obs-studio/) | open-source (GPL-2.0-only) | pacman-repository | Planificado | Streaming |
| Heroic Games Launcher | — | [upstream](https://heroicgameslauncher.com/) | open-source (GPL-3.0-or-later) | none | Solo referencia | Multi-Launcher |
| SteamVR | — | — | — | none | Solo referencia, experimental | VR |

Las entradas de AUR quedan manuales y opcionales: ningún consumidor de
HorneroOS ejecuta recetas de compilación de AUR. Los juegos de Windows y los
binarios comunitarios de compatibilidad nunca se corren como root.

## Base de plataforma

Cada selección de Gaming se apoya en la plataforma neutral al hardware del
catálogo: Mesa/Vulkan (64 bits y 32 bits), `steam-devices`, Feral GameMode,
Gamescope, MangoHud, herramientas Vulkan, PipeWire/WirePlumber y el portal de
escritorio. Los drivers de GPU de cada fabricante son una decisión de hardware
que toman el instalador y los diagnósticos de primer arranque — nunca se
derivan de un ID PCI en este catálogo ni se prometen acá.

## Diagnósticos

Después de instalar un candidato de Gaming, la preparación se consulta con:

```sh
horneroctl gaming doctor
horneroctl gaming doctor --json
```

Doctor informa únicamente capacidades y registro (ICDs de Vulkan, cargador de
32 bits, Steam, GameMode, Gamescope, MangoHud, audio/portal, controles y
preparación de recuperación). Nunca afirma compatibilidad de juegos,
calificación de hardware, rendimiento medido ni latencia.

![Ajustes, página Gaming con los resultados de Gaming doctor. Un aviso indica
el estado de preparación de Gaming y no instala nada hasta que confirmes;
abajo, diecinueve de veinte chequeos pasan, cada uno con un detalle corto en
lenguaje claro.](https://www.horneroos.com/captures/cap-cc-14.png)

*Los mismos chequeos de preparación en Ajustes → Gaming. Gaming es una edición
Soportada: esto informa preparación únicamente y no instala nada. Captura de
escritorio en vivo en el equipo del maintainer, 19 de noviembre de 2026.*

## Límites honestos

- El anti-cheat a nivel de kernel no está soportado. Easy Anti-Cheat y
  BattlEye funcionan solo cuando el editor habilita soporte para Proton.
- Proton lo gestiona Steam; HorneroOS no reemplaza sus componentes DXVK ni
  vkd3d-proton.
- No se activa por defecto ningún ajuste de kernel, planificador, gobernador
  ni memoria.
- VRR y HDR son experimentales y solo tienen sentido en pantallas calificadas;
  los dispositivos handheld requieren calificación por dispositivo (Steam Deck
  es el objetivo de referencia; ROG Ally, Legion Go y otros no se asumen
  compatibles).
- La recuperación gráfica usa el camino existente de actualizaciones/snapshots
  de HorneroOS y un kernel probado; no hay un framework de snapshots exclusivo
  de Gaming.
