# PluginKit 4: la plataforma de extensiones

**Desarrollo.** PluginKit 4 convierte las extensiones de Hornero Shell de "un
widget en unos pocos lugares" en una plataforma: una extensión contribuye a
superficies con nombre mediante contratos tipados, con ajustes que el Centro de
control dibuja por ella. La autoridad de diseño es el
[RFC 0003](rfc-0003-pluginkit-contribution-surfaces.md); el
contrato normativo es `docs/PLUGINS.md` en `HorneroOS/shell`. Esta página es el
recorrido para autoras y autores. Estado: al escribirla, los cambios del Shell
están en revisión; nada de lo que sigue está en un Shell publicado hasta que se
fusionen sus pull requests.

Traduce [development/pluginkit-platform.md](../../development/pluginkit-platform.md);
el inglés es canónico.

## Qué puede contribuir un paquete

- **Widget de escritorio, ítem de barra, tarjeta del dashboard** — Se declara
  en: `surfaces.desktop` / `bar` / `dashboard`; Dónde aparece: la capa de
  escritorio, la barra, el dashboard
- **Varias instancias de un widget de escritorio** — Se declara en:
  `surfaces.desktop.instances`; Dónde aparece: el escritorio; cada instancia
  tiene sus propios ajustes, posición y tamaño
- **Comandos** — Se declara en: `contributes.commands` + `surfaces.commands`;
  Dónde aparece: el lanzador (`>do`), `qs ipc call plugincommands`, atajos de
  teclado que armás vos
- **Mosaico de ajuste rápido** — Se declara en: `contributes.quickSettings` +
  `surfaces.quickSetting`; Dónde aparece: los interruptores rápidos de
  Utilidades, cuando la persona lo agrega
- **Panel del Centro de control** — Se declara en: `contributes.panels` +
  `surfaces.panel`; Dónde aparece: Centro de control › Extensiones, cargado
  solo mientras está abierto
- **Ajustes tipados** — Se declara en: `capabilities.settings`; Dónde aparece:
  controles generados en el Centro de control, con vista previa en vivo

Todo lo que se puede mostrar sin ejecutar código de la extensión (nombres,
glifos, ajustes, lista de comandos) se declara en `manifest.json`; el código se
carga de forma perezosa, por superficie. Un paquete que usa cualquier función
de PluginKit 4 declara `"pluginKit": 4`; el validador rechaza al que declara de
menos, y un Shell más viejo rechaza al paquete que necesita más de lo que tiene.

## Ajustes que se dibujan solos

Además de boolean, integer, number, string y enum, PluginKit 4 suma `colour`,
`list` (selección múltiple), `strings` (lista libre), `text` (varias líneas) y
`path` (una cadena que el Shell nunca abre), y los campos de presentación
`title`, `group`, `unit`, `step`, `visibleWhen` y `hidden` (estado que la
extensión guarda por su cuenta y que nunca se muestra en la interfaz). El Centro
de control los dibuja, valida cada escritura, ofrece Restablecer y muestra la
extensión real arriba de los controles, así cada cambio se ve al instante.

## Configuración por instancia

Una extensión que lee `hostInstanceId` y lo enlaza a `Settings.instanceId`
puede declarar `instances: true`. La persona puede entonces agregar, duplicar,
renombrar y quitar instancias; quitar una borra sus ajustes, posición y tamaño.

## Niveles de PluginKit

`schemaVersion` sigue en `3`. El nivel de capacidades del kit instalado
(`PluginKitInfo.apiLevel`) es contra lo que se compara el entero opcional
`"pluginKit"` del manifiesto (por defecto `3`).

- **Nivel 3 (Signal)** — tema, glifos, las superficies de barra, dashboard,
  escritorio, fondo, lanzador y ajustes, ajustes tipados (booleano, entero,
  número, texto, enum) y las fachadas de datos.
- **Nivel 4 (Platform)** — comandos, mosaicos de ajuste rápido y paneles
  (estos dos están en revisión), esquema de ajustes v2 con vista previa en
  vivo, ajustes ocultos, `strings` y `UiScrollArea` (en revisión), y widgets
  de escritorio por instancia.

El validador calcula el nivel que el manifiesto realmente necesita y rechaza
un paquete que declare menos. En ejecución el Shell omite un paquete que
necesita un kit más nuevo, avisa a la persona que actualice y sigue cargando
los demás. El `docs/PLUGINS.md` del Shell es el contrato; esta página es el
recorrido.

## Confianza

Nada de esto es un sandbox. El QML de la extensión corre dentro del proceso con
tus permisos, igual que antes. PluginKit 4 suma consentimiento y contención:
los mosaicos están apagados hasta que los agregás, los comandos corren solo con
un gesto de la persona, cada superficie tiene su propio Loader para que una
falla quede local, y el modo seguro sigue sin cargar nada. Leé el código de
cualquier extensión antes de habilitarla.
