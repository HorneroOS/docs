# Hornero Apps

Hornero Apps te da un único lugar para descubrir, inspeccionar, instalar,
actualizar y lanzar software desde repositorios de Arch Linux, Flathub,
AppImages, canales oficiales de proveedores y Web Apps aisladas sin tener que
memorizar formatos de empaquetado.

Combina la interfaz Hornero Apps en Quickshell, la integración con el
Lanzador, los perfiles de estación de trabajo de Hornero Welcome y el motor
de línea de comandos `horneroctl store`, respaldado por un catálogo
declarativo firmado (`catalog/apps.v1.json`).

> **Límite de Preview y vuelta atrás:** Hornero Apps **no** crea
> instantáneas del sistema ni ofrece vuelta atrás universal del sistema
> operativo hoy. Las instalaciones y actualizaciones nativas en Arch siguen
> siendo operaciones en un solo sentido sobre el disco; revisá
> [Actualizaciones y recuperación](updates-and-rollback.md) antes de
> modificar paquetes del sistema.

## Descubrimiento unificado entre formatos

En lugar de saltar entre `pacman`, `flatpak`, marcadores del navegador y
binarios sueltos, buscá por nombre de aplicación o categoría de trabajo:

- **Arch nativo (`core`, `extra`, `multilib`):** Binarios rápidos del host
  instalados mediante `pacman` y Polkit (`pkexec`), exigiendo sincronización
  completa del sistema (`-Syu`) para que las actualizaciones parciales no
  rompan bibliotecas compartidas.
- **Flatpak y Flathub:** Aplicaciones de escritorio en sandbox con
  descripciones AppStream y estado explícito de verificación.
- **Canales oficiales de proveedores:** Repositorios firmados de proveedores
  (como el repo Arch de OpenAI para ChatGPT Desktop), repositorios OCI
  Flatpak oficiales (como ArtCraft) y tarballs o instaladores firmados.
- **AppImage:** Ejecutables portables en espacio de usuario guardados en
  `~/Applications`, verificados por SHA-256 cuando hay suma fijada e
  integrados con Gear Lever (`it.mijorus.gearlever`).
- **Web Apps:** Ventanas dedicadas de navegador
  (`hornero-webapp-<id>.desktop`) con perfiles aislados por aplicación para
  separar cookies y permisos.
- **AUR opt-in:** Desactivado por defecto. Las recetas `PKGBUILD` de la
  comunidad requieren habilitación explícita, revisión manual del `PKGBUILD`
  y compilación sin root con `makepkg`.

Snap (`snapd`) viene deshabilitado por defecto y queda fuera del catálogo
estándar.

## Insignias de procedencia y límites honestos

Cada entrada de Hornero Apps muestra una insignia de procedencia para que
sepas quién compiló y firmó el paquete antes de instalarlo.

| Insignia UI | Procedencia en catálogo | Qué significa |
| --- | --- | --- |
| **Oficial** | `arch_official` | Repos `core`, `extra` o `multilib` |
| **Oficial** | `hornero_official` | Compilado en repos de `HorneroOS` |
| **Oficial** | `vendor_official_repo` | Repo firmado o canal OCI oficial |
| **Oficial** | `vendor_official_binary` | Tarball o AppImage firmado |
| **Verificada** | `flathub_verified` | Build de Flathub `verified == true` |
| **Comunidad** | `flathub_community` | Build comunitario sin verificar |
| **Comunidad** | `community_package` | Receta `PKGBUILD` de AUR |
| **Web App** | `official_web_app` | Perfil aislado con `webapp.v` |

Hornero Apps también distingue las **AppImages** y los **paquetes nativos**
(que corren sin sandbox con permisos normales de tu usuario) de las apps
**Flatpak** (que corren confinadas mediante portales).

### Notas honestas de compatibilidad

Que un paquete exista no implica paridad total en Arch Linux:

- **ChatGPT Desktop:** OpenAI ofrece una preview/beta oficial para Linux con
  repositorio Arch firmado (`[openai-chatgpt]`, paquete `chatgpt-bin`, clave
  `3BFA0E4AE8B8CC16A2D9BA684A3B4A566C4660E4`, `x86_64` y `aarch64`). Al ser
  software en preview con repo externo de proveedor, figura como
  `installable_with_limitations`.
- **Claude Desktop:** La beta oficial de Anthropic para Linux soporta solo
  Ubuntu 22.04+ y Debian 12+ (`x64`/`arm64`). **No** existe paquete oficial
  para Arch. En HorneroOS, las vías oficiales del proveedor son **Claude Code
  CLI** (`claude-code`) o **`https://claude.ai`** (`official_web_app`). El
  paquete AUR `claude-desktop` es `community_package` reempaquetando el `.deb`
  (y Cowork exige KVM más 8+ GiB de RAM).
- **Google Antigravity:** Se distribuye en cinco superficies oficiales:
  Antigravity App, Antigravity IDE, Antigravity CLI (`agy`), extensiones de
  IDE (VS Code y JetBrains) y SDK de Python (`google-antigravity`). Las
  compilaciones oficiales de App e IDE para Linux se entregan como `.tar.gz`;
  los paquetes AUR comunitarios pueden quedar desactualizados frente al
  upstream.
- **ArtCraft Launcher y Studio:** No están en Flathub. Upstream publica un
  `.pkg.tar.zst` oficial firmado para Arch, un repo Flatpak OCI oficial
  (`getartcraft.com/artcraft-oci.flatpakrepo`) y AppImage. Sigue siendo un
  opt-in manual experimental; mirá
  [ArtCraft Launcher](../applications/studio-artcraft.md).
- **Anti-cheat en juegos:** El anti-cheat a nivel de kernel no está
  soportado en Linux. Easy Anti-Cheat y BattlEye solo funcionan cuando el
  editor habilita soporte para Proton; mirá
  [Aplicaciones de Gaming](../applications/gaming.md).
- **Sin vuelta atrás universal:** Desinstalar un Flatpak o una WebApp es
  limpio en espacio de usuario, mientras que las transacciones nativas de
  `pacman` modifican la raíz del host sin punto de restauración del sistema.

## Cómo usar Hornero Apps

### Interfaz de Hornero Apps y búsqueda en el Lanzador

Abrí la tienda gráfica desde el Lanzador o directamente desde una terminal:

```sh
horneroctl store gui
```

Dentro del Lanzador (**Ctrl + Space**), escribir el nombre de una aplicación
busca primero en las entradas ya instaladas y muestra debajo coincidencias
instalables del catálogo con su insignia de procedencia. Podés revisar la
cola de instalaciones y actualizaciones de la GUI con
`horneroctl store queue`.

### Perfiles de estación de trabajo en Hornero Welcome

Durante el primer arranque o al preparar una estación nueva, Hornero Welcome
y `horneroctl store profiles` agrupan aplicaciones en perfiles curados (como
Everyday, Developer, Creative Studio, Gaming y AI Workstation). Inspeccioná
un perfil antes de instalar nada:

```sh
horneroctl store profiles
horneroctl store profile-show ai-workstation --json
```

Los perfiles muestran primero cada paquete, origen y licencia, y nunca
instalan software propietario ni entradas AUR sin confirmación explícita.

### Importación de AppImages y Gear Lever

Importá una AppImage de un proveedor a `~/Applications`, verificá su suma
SHA-256 cuando esté fijada y creá su entrada de escritorio XDG:

```sh
horneroctl store appimage list
horneroctl store appimage add ./MiApp.AppImage --sha256 <hex> --yes
```

Hornero Apps chequea el soporte FUSE (`fuse2`/`fuse3`) y se integra con Gear
Lever (`it.mijorus.gearlever`) si está instalado para conservar íconos y
metadatos de actualización. Recordá que las AppImages **no** corren en
sandbox.

### Web Apps con perfiles aislados

Creá o administrá aplicaciones web independientes usando `hornero_core/webapp.v`:

```sh
horneroctl store webapp list
horneroctl store webapp add claude-web \
  --name "Claude" --url "https://claude.ai" --yes
```

Cada WebApp recibe un archivo saneado `hornero-webapp-<id>.desktop` y un
directorio `--user-data-dir` propio, manteniendo cookies de sesión y
permisos separados de tu navegador principal.

### Permisos de Flatpak y Flatseal

Inspeccioná los permisos Flatpak de una aplicación instalada o abrí Flatseal
enfocado en su ID:

```sh
horneroctl store permissions ai.jan.Jan
```

Preferí otorgar permisos puntuales mediante portales (documentos, Wayland,
audio) en lugar de habilitar acceso amplio `--filesystem=host`.

## Referencia CLI (`horneroctl store`)

Todos los comandos de solo lectura soportan `--json`. Los comandos que
modifican el sistema aceptan `--dry-run` para previsualizar cambios y `--yes`
para confirmar la ejecución.

```sh
# Descubrimiento e inspección del catálogo
horneroctl store search "obsidian"
horneroctl store list --category "Creative Studio"
horneroctl store show md.obsidian.Obsidian --json
horneroctl store categories
horneroctl store collections
horneroctl store profiles
horneroctl store profile-show creative-studio

# Estado local, ciclo de vida y lanzamiento
horneroctl store installed
horneroctl store install md.obsidian.Obsidian --dry-run
horneroctl store install md.obsidian.Obsidian --yes
horneroctl store update --dry-run
horneroctl store remove md.obsidian.Obsidian --yes
horneroctl store launch md.obsidian.Obsidian

# Fuentes, formatos, cola, UI y diagnóstico
horneroctl store sources
horneroctl store permissions ai.jan.Jan
horneroctl store appimage list
horneroctl store webapp list
horneroctl store queue
horneroctl store gui
horneroctl store doctor
```

## Provisión para equipos y empresas

Los equipos que administran estaciones compartidas pueden imponer políticas
de confianza, reproducir conjuntos de software de forma declarativa y
auditar cada instalación.

### Políticas de confianza de software (`horneroctl store policy`)

Restringí qué niveles de procedencia y fuentes se pueden instalar en un
equipo:

```sh
# Inspeccionar la política activa
horneroctl store policy show --json

# Permitir solo entradas Oficial y Verificada (Flathub verificado)
horneroctl store policy set --mode verified-only --yes

# Restringir a licencias de código abierto aprobadas por OSI/FSF
horneroctl store policy set --mode open-source-only --yes

# Habilitar solo fuentes explícitas (bloquea AUR y Flathub sin verificar)
horneroctl store policy set \
  --allowed-sources arch_official,hornero_official,flathub_verified --yes
```

La validación de política corre dentro de `horneroctl store` antes de
iniciar cualquier transacción y también impide que asistentes de IA propongan
fuentes no permitidas.

### Manifiestos declarativos (`horneroctl store manifest`)

Exportá la selección de aplicaciones de una máquina y replicala en equipos
nuevos de manera repetible:

```sh
# Exportar apps gestionadas y política a un manifiesto
horneroctl store manifest export ./estacion-equipo.json --yes

# Previsualizar qué instalaría el manifiesto en otro host
horneroctl store manifest apply ./estacion-equipo.json --dry-run

# Importar y aplicar con confirmación explícita
horneroctl store manifest import ./estacion-equipo.json --yes
horneroctl store manifest apply ./estacion-equipo.json --yes
```

### Registro de auditoría (`audit.jsonl`)

Cada mutación de la tienda (`install`, `remove`, `update`, `policy`,
`manifest`, `sources`) agrega un registro JSON estructurado en el directorio
de estado XDG del usuario (`~/.local/state/hornero/store/audit.jsonl`) con
marca de tiempo, acción, ID de aplicación, fuente resuelta, procedencia,
decisión de política y resultado.

## Contribución y gobernanza del catálogo

Las aplicaciones de Hornero Apps viven en `catalog/apps.v1.json`. Quienes
contribuyen agregan o actualizan entradas mediante pull requests y nunca con
ediciones ad-hoc.

### Reglas de envío

1. **Solo identificadores verificados:** Incluí nombres exactos de paquetes
   de Arch, IDs de Flathub, URLs oficiales de releases del proveedor o URLs
   oficiales de web apps.
2. **Procedencia y estado precisos:** Usá la taxonomía de 8 niveles y marcá
   con honestidad las apps en preview, experimentales o limitadas por distro
   como `installable_with_limitations`, `community_maintained` o
   `guided_setup_required`.
3. **Licencias y marcas registradas:** Registrá el identificador SPDX exacto
   o la clase propietaria. Nunca agregues espejos de binarios propietarios ni
   incluyas paquetes de Chaotic-AUR como `arch_official`.
4. **Validación automática en CI:** Cada PR al catálogo corre validación de
   esquema, chequeos en vivo contra los índices de Arch, Flathub API v2
   (campo `verified`) y AUR RPC v5, más controles de licencia/marca antes de
   que los mantenedores firmen el catálogo publicado con `minisign`.

## Guías relacionadas

- [ADR: arquitectura de Hornero Apps (en inglés)](../../architecture/adr-hornero-apps.md)
- [Modelo de amenazas de Hornero Apps (en inglés)](../../architecture/hornero-apps-threat-model.md)
- [Resumen CLI de `horneroctl`](horneroctl.md)
- [Seguridad y privacidad](../security/README.md)
- [Actualizaciones y recuperación](updates-and-rollback.md)
