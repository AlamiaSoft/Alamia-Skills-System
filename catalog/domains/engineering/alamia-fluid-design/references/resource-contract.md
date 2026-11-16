# Resource contract

This note defines how agents should consume the assets shipped with Alamia Fluid Design.

## CSS loading and ownership

1. Inspect the host application's reset, token layer, CSS framework, and theme mechanism.
2. Reuse the host system when it already provides equivalent primitives. Bundled files are references, not mandatory dependencies.
3. If both bundled CSS files are used, load `tokens.css` first and `fluid-engine.css` second. Load application component styles after both.
4. Resolve duplicate token names explicitly. Do not silently redefine the host application's semantic colors or typography.
5. Do not copy the global reset into a mature application without reviewing its effects on lists, controls, dialogs, media, and third-party widgets.

## Fluid CSS primitives

- `.fluid-shell*`: centered content shells with fluid gutters and maximum widths.
- `.fluid-grid*`: intrinsic grid primitives. Set `--grid-min-item` to the real minimum useful card width.
- `.fluid-flex-wrap` and `.fluid-flex-between`: wrapping action/tool groups.
- `.container-query-root` and `.cq-panel`: establish inline-size query contexts.
- `.fluid-split`: switches from stacked to row layout at 680px of its nearest eligible ancestor container. Its parent must establish a container context.
- `.fluid-subgrid-card`: progressive enhancement only. The parent grid must define matching row tracks and each card must span the intended number of rows. Provide a fallback.
- `.safe-top` / `.safe-bottom`: safe-area-aware padding; avoid stacking these with existing app insets accidentally.

Utilities are not a complete component library. Verify the resulting cascade and layout in the host application.

## JavaScript diagnostics contract

`engine/fluid-engine.js` is optional diagnostics code:
- Importing the module has no side effects.
- Instantiate `new FluidEngine(options)` and call `.init()` explicitly.
- Inspector is disabled by default. Enable it only in development with `{ enableInspector: true }`.
- Hero telemetry is disabled by default. Enable with `{ updateHeroTelemetry: true }` only on the showcase page that contains its documented telemetry IDs.
- `.destroy()` removes listeners and the inspector element.
- `.toggleTheme()` is a demo helper, not a complete production theme manager.
- Do not use viewport categories to select application layout. CSS remains authoritative.

Example:

```js
import { FluidEngine } from './engine/fluid-engine.js';

const diagnostics = new FluidEngine({ enableInspector: true });
diagnostics.init();

// When the development surface is torn down:
diagnostics.destroy();
```

Examples are implementation references, not proof of cross-browser conformance. Run and test an example before describing it as validated.
