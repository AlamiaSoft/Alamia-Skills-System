---
name: alamia-fluid-design
description: >-
  Design, implement, and validate production-ready responsive web interfaces and PWAs across narrow foldables, mobile, split-screen, desktop, and ultrawide displays using fluid scales, intrinsic layouts, container queries, accessible interaction patterns, and evidence-based viewport testing.
license: MIT
metadata:
  type: specialist-capability
  category: engineering
  domain: product-engineering
  version: "1.2.0"
---

# Alamia Fluid Design

## Purpose

Design, implement, and verify frontend interfaces that adapt to available space, input method, orientation, user preferences, and content—not merely named device classes. The target range is 280px through 3840px+, including narrow split-screen panes, short landscape viewports, zoomed layouts, and installed PWAs.

A layout is not complete because its CSS uses `clamp()` or because it looks good at one mobile and one desktop width. Completion requires testing the actual rendered application and recording the limits of that verification.

## Activation

Use this skill when building or revising responsive websites, application shells, dashboards, admin panels, data-heavy interfaces, PWAs, mobile-first workflows, product configurators, or components that must work in variable-width containers.

## Inputs and assumptions

Inspect the actual project before changing it:
- Framework, build system, CSS strategy, existing design tokens, component library, routing, and responsive conventions.
- Product requirements, content hierarchy, user journeys, wireframes, screenshots, and target interaction modes.
- Required browser support and whether the application is an installed PWA.
- Existing tests, browser automation, linting, and visual-regression infrastructure.

Do not introduce a second design system or overwrite project conventions merely to use sample assets. If the project already has tokens or components, map the fluid principles onto those primitives.

## Resource map and correct asset use

This skill ships reusable reference assets under `engine/` and examples under `examples/`:

| Asset | Intended use |
|---|---|
| `engine/tokens.css` | Optional semantic color, typeface, radius, shadow, and transition tokens |
| `engine/fluid-engine.css` | Optional fluid scales, shells, intrinsic grids, helpers, and accessibility primitives |
| `engine/fluid-engine.js` | Optional viewport metrics and development inspector; not required for responsive CSS |
| `examples/index.html` | Interactive showcase and container-query playground |
| `examples/analytics-dashboard/index.html` | Dashboard layout reference |
| `examples/game-pwa/index.html` | Compact game/PWA reference |
| `examples/product-configurator/index.html` | Configurator reference, when present |

If using both CSS files, load tokens first, then the engine stylesheet, then application/component styles. Inspect the host application's reset, token layer, and theme strategy first. Do not copy the full stylesheet blindly or overwrite an established design system.

The JavaScript module is optional and must be explicitly initialized. It is diagnostics, not layout infrastructure. Inspector and demo telemetry are disabled by default. Do not make production layout or interaction depend on its viewport categories. See `references/resource-contract.md`.

## Design and implementation procedure

### 1. Discover content and constraints

Identify primary tasks, essential information/actions/navigation, minimum useful component widths, and what can wrap, stack, collapse, move into a drawer, or scroll within a bounded region. Include keyboard, screen-reader, touch, pointer, zoom, and reduced-motion requirements.

Use content-fit thresholds rather than device labels. A breakpoint is justified when the composition stops working.

### 2. Establish fluid scales

Use CSS `clamp()` for typography, spacing, gutters, and dimensions that should interpolate. Define minimum and maximum values deliberately; not every property should grow with viewport width. Keep body copy readable (often around 60–70ch) and avoid oversized type on short or narrow screens.

```css
:root {
  --page-gutter: clamp(1rem, 0.7rem + 1.5vw, 2rem);
  --section-space: clamp(1.5rem, 1rem + 2vw, 3rem);
  --heading-size: clamp(1.75rem, 1.2rem + 2vw, 3rem);
}
```

### 3. Prefer intrinsic layout primitives

Use `minmax(0, 1fr)` for flexible grid tracks, `min-width: 0` on grid/flex children with potentially wide content, and `min(100%, <preferred-minimum>)` to prevent intrinsic columns exceeding narrow parents. Use `auto-fit` / `auto-fill` only when content supports independent columns. Let action groups wrap. Do not force every dashboard to remain multi-column on narrow screens.

### 4. Use container queries correctly

Set `container-type: inline-size` on the component's containing context, not on the element that needs to query itself. Rules only work when an ancestor establishes the query container. The shipped `.fluid-split` utility expects an ancestor with `.container-query-root` or `.cq-panel`. Use named containers where nested contexts could select the wrong ancestor. Provide a sensible base layout.

### 5. Design responsive navigation and application shells

Preserve access to primary destinations. Choose wrapping navigation, an accessible disclosure/drawer, or bottom navigation based on task frequency and information architecture. Preserve active location, focus order, Escape behavior, expanded state, and focus return. Do not rely on hover alone or hide critical navigation on mobile.

### 6. Handle data, charts, filters, and forms intentionally

- **Tables:** retain semantic markup. Choose bounded horizontal scrolling, a justified priority-column strategy, or a labelled card transformation. Never silently discard critical data. Make scroll regions discoverable and keyboard-accessible when needed.
- **Charts:** bound the parent, use responsive SVG/viewBox or canvas sizing, preserve useful labels/legends, and provide a textual summary or data alternative.
- **Filters/toolbars:** wrap or move secondary filters into a disclosure; keep applied-filter state and reset action discoverable.
- **Forms:** use single-column flow in narrow containers, persistent labels, appropriate input types, associated errors, and clear actions. Do not let sticky footers cover fields or the virtual keyboard.
- **Long identifiers/content:** use deliberate wrapping or bounded overflow; do not let min-content sizing expand the page.

See `references/responsive-patterns.md`.

### 7. Apply PWA and input ergonomics

Use a correct viewport meta tag and safe-area insets where edge-to-edge display is intended. Prefer `100dvh` with a `100vh` fallback for full-height shells. Do not disable browser zoom with `user-scalable=no`. Test software-keyboard behavior on supported browsers/devices; a viewport meta hint is not proof. Aim for 44×44 CSS px touch targets where practical and meet applicable WCAG 2.2 requirements. Support keyboard navigation, visible focus, reduced motion, forced colors, and adequate contrast.

### 8. Treat edge cases as first-class

Test short landscape heights, narrow split-screen panes, 200% zoom, large text, long translated strings, empty/loading/error states, dense data, and foldable viewport segments where supported. Foldable segment APIs are progressive enhancements, not baseline dependencies.

### 9. Validate the rendered application

Follow `references/validation-protocol.md`. Test the actual app at representative widths from 280px to 3840px, including intermediate widths around layout transitions. Check page and component overflow; do not use `overflow-x: hidden` or `clip` to conceal unresolved defects. Test keyboard, focus, zoom, reduced motion, forced colors, coarse pointer, console errors, and failed assets. Capture screenshots when browser tooling is available. Record browser, viewport, method, failures, and untested cases. Never claim browser validation from source inspection alone.

## Outputs

Deliver the host-project implementation, which may include adapted tokens, fluid CSS primitives, responsive components, accessible interaction behavior, tests, and a concise validation report. State what passed, failed, and remains unverified.

Do not add `fluid-engine.js` to a production bundle unless diagnostics are genuinely needed. CSS alone should provide responsive behavior.

## Quality gate

- [ ] No unexpected page-level horizontal overflow; component-level overflow is intentional, bounded, and usable.
- [ ] Layouts adapt to available component width, not only viewport width.
- [ ] Primary tasks, navigation, and essential data remain available on narrow screens.
- [ ] No fixed-width main wrappers or unexplained breakpoint proliferation.
- [ ] Tables, charts, long strings, and nested grid/flex children do not blow out tracks.
- [ ] Keyboard focus, semantics, labels, touch targets, contrast, reduced motion, and forced-colors behavior are considered.
- [ ] Virtual keyboard and sticky/fixed action areas do not obscure essential controls.
- [ ] No console errors or failed critical assets in tested flows.
- [ ] Validation evidence and limitations are reported honestly.

## Boundaries

- Do not replace a working project design system without a clear migration reason.
- Do not hide critical content or functionality to make a screenshot fit.
- Do not use `overflow: hidden/clip` as a substitute for fixing overflow.
- Do not use viewport breakpoints where a component query is the correct abstraction.
- Do not add mandatory dependencies or browser automation tooling without approval.
- Do not claim production readiness merely because a sample or skill file exists.
