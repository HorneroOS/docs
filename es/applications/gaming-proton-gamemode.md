# Gaming: Proton, GameMode, Gamescope y MangoHud

Cómo correr juegos en HorneroOS y cómo distinguir un problema de
juego de uno de sistema. HorneroOS no publica acá claims de
performance ni de frames: medí tu máquina, con tus juegos.

## Revisá primero si está listo

```sh
horneroctl gaming doctor
horneroctl mode set gaming
horneroctl gaming selection show
```

El doctor reporta solo capacidad y registro: Vulkan, loader de
32 bits, Steam, GameMode, Gamescope, MangoHud, audio y controles.
Nunca afirma que un juego va a correr ni a qué velocidad.

![Página Gaming de Settings con resultados del doctor. Un aviso
dice que Gaming no instala nada hasta que confirmes; abajo,
diecinueve de veinte chequeos pasan con detalle en lenguaje
llano.](https://www.horneroos.com/captures/cap-cc-14.png)

*Los mismos chequeos en Settings → Gaming. Reporta preparación,
no instala nada. Captura de la máquina del mantenedor,
19 de noviembre de 2026.*

## Steam y Proton

Steam es opt-in; instalalo solo si lo querés. Proton lo gestiona
Steam: elegí la versión por juego en Propiedades → Compatibilidad
y cambiá una cosa por vez.

- Opciones de lanzamiento en Propiedades → General del juego.
  El patrón oficial es variables primero y `%command%` donde
  corresponde, por ejemplo variables de offload en una laptop
  híbrida (mirá [Gráficos híbridos y NVIDIA](../hardware/hybrid-graphics-nvidia.md)
  en la guía de hardware).
- Leé las opciones registradas por HorneroOS con
  `horneroctl gaming launch-options` antes de inventar flags.
- Activá el pre-caching de shaders de Steam y esperá que termine
  antes de juzgar tirones del primer lanzamiento.
- Para un juego que no arranca, activá el log de Proton desde
  sus opciones y guardá el log que Steam escribe en tu home.

## GameMode, MangoHud y Gamescope: de a uno

- GameMode es parte de la base de plataforma. Sumalo a un solo
  juego y medí ese juego; no apiles todas las herramientas y
  después adivines cuál ayudó o empeoró.
- MangoHud es un overlay para medir frame times. Juzgá la
  fluidez por el gráfico de frame times en tu sesión, no por un
  promedio publicado por otra persona.
- Gamescope corre un juego en su propia sesión anidada, útil
  para límites de resolución y frames que vos definís. Partí
  de su sesión por defecto y agregá una opción por vez.

El modo Gaming automático se elige con
`horneroctl mode set gaming`; cambia el modo de escritorio, no
la compatibilidad de un juego.

## Launchers más allá de Steam

Lutris, Bottles, Wine y Heroic están planificados o son solo
referencia en la [matriz Gaming](../../applications/gaming.md),
no soporte Gaming instalado. Que un título funcione en un launcher
instalado a mano es tu configuración funcionando, no una
garantía de HorneroOS.

## Límites honestos

- El anti-cheat a nivel kernel no está soportado. Easy
  Anti-Cheat y BattlEye solo funcionan donde el publisher
  habilita soporte Proton.
- Proton lo gestiona Steam; HorneroOS no reemplaza DXVK ni
  vkd3d-proton.
- Ningún tweak de kernel, scheduler ni governor viene activado
  por defecto, y ninguno se recomienda acá sin tu medición.
- VRR y HDR son experimentales y necesitan pantalla cualificada.
