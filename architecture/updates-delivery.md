# Packaging and delivery

HorneroOS is assembled from several repositories and packages. This page is
for contributors changing how source reaches an installed system; it is not
an end-user installation guide. The project does not currently publish a
supported installable ISO. See [Getting started](../getting-started/README.md)
for the current status.

## Delivery boundaries

| Source | Delivered responsibility |
| --- | --- |
| [`config`](https://github.com/HorneroOS/config) | Defaults, theme packs, assets, and system configuration materialization. |
| [`shell`](https://github.com/HorneroOS/shell) | Quickshell runtime and its services/modules. |
| [`hornero`](https://github.com/HorneroOS/hornero) | `horneroctl` and supported OS-facing operations. |
| [`greeter`](https://github.com/HorneroOS/greeter) | Hornero's SDDM greeter theme package. |
| [`website`](https://github.com/HorneroOS/website) | Public product information and reviewed pins to source data and docs. |

Repository releases, package recipes, and cross-repository pins are the
delivery contract. Check the current release page before presenting any
package as generally available. Do not infer a supported installation path
from the fact that an individual component can be packaged.

## User data and shipped defaults

Treat `/usr/share` content as package-owned and read-only. User changes belong
in the documented user configuration/data locations. Package updates must
not silently rewrite user-owned files. Validate changed defaults in a fresh
package-faithful environment, preserve explicit user overrides, and avoid
carrying obsolete paths or formats forward without a supported in-place
update contract. Never copy a developer's machine-specific files into
package defaults.

## Release validation

Before a release or pin update, verify the exact source revisions, package
contents, dependency declarations, and a clean package-faithful environment.
For changes that cross repositories, update pins only after the source change
is reviewed and merged. Use the existing Hornero QA project for graphical
acceptance where applicable; do not substitute a developer's dotfiles for
packaged product dependencies.

The detailed package and release workflow belongs in each implementing
repository's contributor docs. This handbook records the boundaries and
links rather than duplicating those procedures.
