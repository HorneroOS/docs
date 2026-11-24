# Creá tu propio compañero de escritorio

Esta guía lleva a una artista o desarrolladora desde el arte
terminado hasta un compañero caminando en un escritorio HorneroOS.
No hace falta saber QML del Shell: un paquete de compañero es
**solo datos** — definiciones JSON más sprites PNG/WebP,
renderizados por componentes nativos confiables. El contrato
normativo vive en el repositorio del Shell
(`docs/COMPANION_PLATFORM.md`); esta página es el recorrido
práctico.

## 1. Prepará el arte

- Un modelo de personaje consistente: mismas proporciones, paleta
  y luz en cada pose. Diseñá primero para 64–256 píxeles lógicos;
  una ilustración de 1024 px que se vuelve barro a 128 px todavía
  no es un sprite de escritorio.
- Frames PNG o WebP transparentes sobre un canvas compartido (por
  ejemplo 512 × 512), o un atlas de sprites con grilla regular.
  Todas las poses sobre la misma línea de suelo, con anclas
  `ground` y `center` registradas.
- Solo `idle` es obligatorio. Sumá las acciones semánticas que tu
  personaje soporta de verdad (`walk`, `greet`, `sleep`, `think`,
  …). Una acción faltante cae dentro de la misma apariencia,
  nunca a otra apariencia ni a otro personaje.
- Las apariencias (skins) son variaciones visuales completas del
  mismo personaje. Una skin sin una acción muestra su propio idle
  en vez de pedir prestado un frame sin la ropa.

## 2. Armá el paquete

```text
mi-companero/
  manifest.json
  Main.qml            (andamiaje inerte canónico, nunca se carga)
  README.md
  LICENSE
  companions/<id-del-personaje>/
    companion.json
    frames/*.png
```

El manifiesto del plugin declara PluginKit 6 y `dataOnly`:

```json
{
  "schemaVersion": 3,
  "pluginKit": 6,
  "dataOnly": true,
  "id": "mi-companero",
  "name": "Mi Compañero",
  "version": "1.0.0",
  "description": "Un compañero de escritorio solo-datos.",
  "author": "Tu nombre",
  "license": "MIT",
  "entrypoint": "Main.qml",
  "placement": "background",
  "files": [
    "Main.qml", "README.md", "LICENSE",
    "companions/capi/companion.json",
    "companions/capi/frames/idle-01.png"
  ],
  "capabilities": {"processCommands": [], "networkHosts": [], "settings": {}},
  "contributes": {
    "companions": [{
      "id": "capi",
      "title": "Capi",
      "definition": "companions/capi/companion.json",
      "preview": "companions/capi/frames/idle-01.png"
    }]
  }
}
```

`Main.qml` tiene que ser byte a byte el andamiaje canónico del
ejemplo; el Shell nunca lo instancia. Cualquier otro QML, comando
de proceso, host de red, ajuste, acción o superficie ejecutable
rechaza la clasificación solo-datos.

## 3. Escribí la definición del personaje

`companion.json` es un documento cerrado y versionado
(`schemas/companion-definition.schema.json` en el Shell): nombres
localizados, procedencia de autor/licencia, preview, canvas y
anclas, capacidades, skins con animaciones semánticas, y
opcionalmente hábitat, personalidades (rasgos y frases fijas;
nunca prompts ni herramientas) y compatibilidad de asistente.
Los presupuestos se controlan al instalar: dimensiones y píxeles
decodificados, cantidad de frames y duraciones están acotados, y
cada asset referenciado tiene que ser un archivo local listado.
Los assets remotos se rechazan.

Copiá `examples/plugins/example-companion` del Shell como punto
de partida; trae dos personajes completos.

## 4. Validá e instalá

```bash
horneroctl plugin install-local ./mi-companero --yes
horneroctl plugin enable mi-companero --yes
qs ipc call plugins reload
```

La validación corre durante la instalación; el validador del
Shell es la autoridad de admisión. Cuando la instalación te pida
registrar confianza para el payload, seguí su indicación antes
de habilitar.

Después abrí Centro de Control → Compañeros: tu personaje aparece
en la colección. **Agregar al escritorio** crea una instancia
independiente con su apariencia, monitor, tamaño, hábitat y
reacciones propios. Quitar el paquete deja los registros de
instancias como no disponibles en vez de borrar configuración
ajena.

## 5. Publicá

Los paquetes comunitarios van por el flujo del catálogo de
HorneroOS/plugins (validación de manifiesto, regeneración del
catálogo, motivos de permisos bilingües, registro de calidad).
Publicá solo arte que tengas derecho a redistribuir; un personaje
instalado en privado nunca necesita el catálogo. Mantené licencia
y atribución en la procedencia de la definición — el Shell muestra
la autoría del paquete, no puede otorgar derechos que no tenés.

## Problemas frecuentes

- **La validación nombra un presupuesto:** achicá frames o partí
  el paquete; el error dice el límite exacto que saltó.
- **El personaje no aparece en la colección:** corré
  `qs ipc call plugins status` y buscá el diagnóstico del paquete;
  una definición mal formada se omite, nunca es fatal.
- **Los pies flotan o se hunden:** tu ancla `ground` tiene que
  estar sobre la fila de contacto con el suelo; todas las poses
  comparten un canvas.
- **Bordes lavados:** exportá con alfa recto y mates limpios;
  evitá el derrame verde de fuentes chroma-key.
